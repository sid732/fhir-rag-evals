"""SQLite storage for resources, cards and embeddings (design.md D8).

One file holds everything the service reads. Embeddings are keyed by
(model, SHA-256 of the card text), so rebuilding the index only re-embeds
cards whose text changed; CI caches the file between runs.
"""

import hashlib
import json
import sqlite3
import threading
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import numpy.typing as npt

from fhir_rag.fhir.cards import Chunk
from fhir_rag.fhir.loader import Resource

type Matrix = npt.NDArray[np.float32]

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS patients (
    patient_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    gender TEXT,
    birth_date TEXT
);
CREATE TABLE IF NOT EXISTS resources (
    ref TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    resource_type TEXT NOT NULL,
    json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS chunks (
    chunk_id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    resource_ref TEXT NOT NULL,
    resource_type TEXT NOT NULL,
    date TEXT,
    text TEXT NOT NULL,
    series_key TEXT,
    text_sha TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS chunks_by_patient ON chunks (patient_id);
CREATE TABLE IF NOT EXISTS pinned (
    patient_id TEXT NOT NULL,
    position INTEGER NOT NULL,
    ref TEXT NOT NULL,
    PRIMARY KEY (patient_id, position)
);
CREATE TABLE IF NOT EXISTS embeddings (
    model TEXT NOT NULL,
    text_sha TEXT NOT NULL,
    vector BLOB NOT NULL,
    PRIMARY KEY (model, text_sha)
);
"""


def text_sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


@dataclass(frozen=True)
class PatientRow:
    patient_id: str
    name: str
    gender: str | None
    birth_date: str | None


@dataclass(frozen=True)
class StoredChunk:
    patient_id: str
    chunk: Chunk


class Store:
    """Thread-safe wrapper around one SQLite connection.

    The API reads from worker threads, so every query takes the lock;
    queries are short and the service is read-mostly.
    """

    def __init__(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        self._db = sqlite3.connect(path, check_same_thread=False)
        self._db.executescript(SCHEMA)
        self._lock = threading.Lock()

    def close(self) -> None:
        self._db.close()

    # --- writes (ingest) ---

    def reset_records(self) -> None:
        """Delete patients, resources and cards; keep cached embeddings."""
        with self._lock, self._db:
            self._db.execute("DELETE FROM patients")
            self._db.execute("DELETE FROM resources")
            self._db.execute("DELETE FROM chunks")
            self._db.execute("DELETE FROM pinned")

    def add_patient(self, row: PatientRow) -> None:
        with self._lock, self._db:
            self._db.execute(
                "INSERT INTO patients VALUES (?, ?, ?, ?)",
                (row.patient_id, row.name, row.gender, row.birth_date),
            )

    def add_resources(self, patient_id: str, resources: Iterable[Resource]) -> None:
        rows = [
            (
                f"{r['resourceType']}/{r['id']}",
                patient_id,
                r["resourceType"],
                json.dumps(r),
            )
            for r in resources
        ]
        with self._lock, self._db:
            self._db.executemany("INSERT INTO resources VALUES (?, ?, ?, ?)", rows)

    def add_chunks(self, patient_id: str, chunks: Iterable[Chunk]) -> None:
        rows = [
            (
                c.chunk_id,
                patient_id,
                c.resource_ref,
                c.resource_type,
                c.date,
                c.text,
                c.series_key,
                text_sha(c.text),
            )
            for c in chunks
        ]
        with self._lock, self._db:
            self._db.executemany("INSERT INTO chunks VALUES (?, ?, ?, ?, ?, ?, ?, ?)", rows)

    def add_pinned(self, patient_id: str, refs: list[str]) -> None:
        """The patient's summary cards (fhir_rag.retrieval.summary), in order."""
        rows = [(patient_id, i, ref) for i, ref in enumerate(refs)]
        with self._lock, self._db:
            self._db.executemany("INSERT INTO pinned VALUES (?, ?, ?)", rows)

    def set_meta(self, key: str, value: str) -> None:
        with self._lock, self._db:
            self._db.execute("INSERT OR REPLACE INTO meta VALUES (?, ?)", (key, value))

    def missing_embeddings(self, model: str) -> list[tuple[str, str]]:
        """(text_sha, text) for card texts with no vector for this model yet."""
        with self._lock:
            rows = self._db.execute(
                """SELECT DISTINCT c.text_sha, c.text FROM chunks c
                   LEFT JOIN embeddings e ON e.model = ? AND e.text_sha = c.text_sha
                   WHERE e.text_sha IS NULL ORDER BY c.text_sha""",
                (model,),
            ).fetchall()
        return [(sha, text) for sha, text in rows]

    def add_embeddings(self, model: str, shas: list[str], vectors: Matrix) -> None:
        rows = [
            (model, sha, vec.astype(np.float32).tobytes())
            for sha, vec in zip(shas, vectors, strict=True)
        ]
        with self._lock, self._db:
            self._db.executemany("INSERT OR REPLACE INTO embeddings VALUES (?, ?, ?)", rows)

    def prune_embeddings(self) -> int:
        """Drop vectors no current card uses; returns how many were dropped."""
        with self._lock, self._db:
            cursor = self._db.execute(
                "DELETE FROM embeddings WHERE text_sha NOT IN (SELECT text_sha FROM chunks)"
            )
        return cursor.rowcount

    # --- reads (service) ---

    def meta(self, key: str) -> str | None:
        with self._lock:
            row = self._db.execute("SELECT value FROM meta WHERE key = ?", (key,)).fetchone()
        return row[0] if row else None

    def patients(self) -> list[PatientRow]:
        with self._lock:
            rows = self._db.execute("SELECT * FROM patients ORDER BY patient_id").fetchall()
        return [PatientRow(*row) for row in rows]

    def patient(self, patient_id: str) -> PatientRow | None:
        with self._lock:
            row = self._db.execute(
                "SELECT * FROM patients WHERE patient_id = ?", (patient_id,)
            ).fetchone()
        return PatientRow(*row) if row else None

    def resource(self, ref: str) -> tuple[str, Resource] | None:
        """(patient_id, resource JSON) for a reference like "Observation/<id>"."""
        with self._lock:
            row = self._db.execute(
                "SELECT patient_id, json FROM resources WHERE ref = ?", (ref,)
            ).fetchone()
        if row is None:
            return None
        resource: Resource = json.loads(row[1])
        return row[0], resource

    def chunks(self, patient_id: str) -> list[Chunk]:
        """All cards for one patient, in a stable order."""
        with self._lock:
            rows = self._db.execute(
                """SELECT chunk_id, resource_ref, resource_type, date, text, series_key
                   FROM chunks WHERE patient_id = ? ORDER BY chunk_id""",
                (patient_id,),
            ).fetchall()
        return [Chunk(*row) for row in rows]

    def pinned(self, patient_id: str) -> list[str]:
        with self._lock:
            rows = self._db.execute(
                "SELECT ref FROM pinned WHERE patient_id = ? ORDER BY position",
                (patient_id,),
            ).fetchall()
        return [ref for (ref,) in rows]

    def chunk_owner(self, chunk_id: str) -> str | None:
        with self._lock:
            row = self._db.execute(
                "SELECT patient_id FROM chunks WHERE chunk_id = ?", (chunk_id,)
            ).fetchone()
        return row[0] if row else None

    def embeddings(self, patient_id: str, model: str) -> tuple[list[str], Matrix]:
        """chunk_ids and their vectors (one row each) for one patient."""
        with self._lock:
            rows = self._db.execute(
                """SELECT c.chunk_id, e.vector FROM chunks c
                   JOIN embeddings e ON e.model = ? AND e.text_sha = c.text_sha
                   WHERE c.patient_id = ? ORDER BY c.chunk_id""",
                (model, patient_id),
            ).fetchall()
        if not rows:
            return [], np.zeros((0, 0), dtype=np.float32)
        matrix = np.stack([np.frombuffer(blob, dtype=np.float32) for _, blob in rows])
        return [chunk_id for chunk_id, _ in rows], matrix
