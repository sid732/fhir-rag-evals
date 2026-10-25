"""Patient-scoped retrieval (PLAN.md D5, D6).

Every query is filtered to one patient's cards before any scoring, so another
patient's record can never reach the prompt. Within that patient:

1. rank with BM25, dense cosine similarity, or both fused with RRF;
2. optionally expand series: when a card belongs to a series (every HbA1c
   result, every prescription of one drug), add that series' newest members
   right after it, and skip the series' other members. Plain similarity can't
   tell the newest HbA1c from a 2019 one, since their cards differ only in
   date; expansion makes "most recent" and "trend" questions answerable from
   the context, and the skip stops one series from filling every slot;
3. optionally put the pinned patient summary (fhir_rag.retrieval.summary)
   in front. Summary cards don't count against k.
"""

import threading
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import Literal

import numpy as np

from fhir_rag.config import RetrievalMode
from fhir_rag.fhir.cards import Chunk
from fhir_rag.retrieval.bm25 import BM25Index
from fhir_rag.retrieval.dense import DenseIndex, Embedder
from fhir_rag.retrieval.fusion import rrf
from fhir_rag.store import Store


@dataclass(frozen=True)
class RetrievalConfig:
    mode: RetrievalMode = "hybrid"
    k: int = 10
    candidates: int = 50  # per ranker, before fusion
    series_expansion: int = 3  # 0 turns it off
    pin_summary: bool = True


type Source = Literal["summary", "ranked", "series"]


@dataclass(frozen=True)
class Retrieved:
    chunk: Chunk
    rank: int  # 1-based position in the final list
    score: float  # BM25, cosine, or RRF score of the card that brought it in; 0 for summary
    source: Source  # pinned summary, ranked directly, or added by series expansion


@dataclass
class PatientIndex:
    chunks: list[Chunk]
    bm25: BM25Index
    dense: DenseIndex | None
    pinned_refs: list[str] = field(default_factory=list)
    by_id: dict[str, Chunk] = field(default_factory=dict)
    series: dict[str, list[Chunk]] = field(default_factory=dict)  # newest first

    def __post_init__(self) -> None:
        self.by_id = {c.chunk_id: c for c in self.chunks}
        grouped: dict[str, list[Chunk]] = {}
        for chunk in self.chunks:
            if chunk.series_key:
                grouped.setdefault(chunk.series_key, []).append(chunk)
        self.series = {
            key: sorted(members, key=lambda c: (c.date or "", c.chunk_id), reverse=True)
            for key, members in grouped.items()
        }


class UnknownPatientError(KeyError):
    pass


class Retriever:
    def __init__(self, store: Store, embedder: Embedder | None, cache_size: int = 32):
        self._store = store
        self._embedder = embedder
        self._cache: OrderedDict[str, PatientIndex] = OrderedDict()
        self._cache_size = cache_size
        self._lock = threading.Lock()  # the API calls retrieve() from worker threads

    def index(self, patient_id: str) -> PatientIndex:
        with self._lock:
            return self._index(patient_id)

    def _index(self, patient_id: str) -> PatientIndex:
        if patient_id in self._cache:
            self._cache.move_to_end(patient_id)
            return self._cache[patient_id]
        chunks = self._store.chunks(patient_id)
        if not chunks:
            raise UnknownPatientError(patient_id)
        dense = None
        if self._embedder is not None:
            ids, matrix = self._store.embeddings(patient_id, self._embedder.model_name)
            if len(ids) != len(chunks):
                raise RuntimeError(
                    f"{len(chunks) - len(ids)} cards have no {self._embedder.model_name} "
                    "vector; run `make ingest`"
                )
            dense = DenseIndex(ids, matrix)
        bm25 = BM25Index([c.chunk_id for c in chunks], [c.text for c in chunks])
        index = PatientIndex(chunks, bm25, dense, self._store.pinned(patient_id))
        self._cache[patient_id] = index
        if len(self._cache) > self._cache_size:
            self._cache.popitem(last=False)
        return index

    def _bm25_ranking(self, index: PatientIndex, query: str, n: int) -> list[tuple[str, float]]:
        scores = index.bm25.scores(query)
        hits = [i for i in np.flatnonzero(scores > 0)]
        # Ties (cards that differ only in date) go to the newer card.
        hits.sort(
            key=lambda i: (
                -scores[i],
                _negated_date(index.chunks[i].date),
                index.chunks[i].chunk_id,
            )
        )
        return [(index.chunks[i].chunk_id, float(scores[i])) for i in hits[:n]]

    def _dense_ranking(self, index: PatientIndex, query: str, n: int) -> list[tuple[str, float]]:
        dense = index.dense
        if dense is None or self._embedder is None:
            raise RuntimeError("dense retrieval needs an embedder")
        scores = dense.scores(self._embedder.embed_query(query))
        order = sorted(range(len(scores)), key=lambda i: (-scores[i], dense.chunk_ids[i]))
        return [(dense.chunk_ids[i], float(scores[i])) for i in order[:n]]

    def retrieve(self, patient_id: str, query: str, config: RetrievalConfig) -> list[Retrieved]:
        index = self.index(patient_id)
        if config.mode == "bm25":
            ranked = self._bm25_ranking(index, query, config.candidates)
        elif config.mode == "dense":
            ranked = self._dense_ranking(index, query, config.candidates)
        else:
            bm25 = self._bm25_ranking(index, query, config.candidates)
            dense = self._dense_ranking(index, query, config.candidates)
            ranked = rrf([[c for c, _ in bm25], [c for c, _ in dense]])
        return _assemble(index, ranked, config)


def _negated_date(date: str | None) -> tuple[int, ...]:
    """Sort key that puts later dates first."""
    return tuple(-ord(ch) for ch in (date or ""))


def _assemble(
    index: PatientIndex, ranked: list[tuple[str, float]], config: RetrievalConfig
) -> list[Retrieved]:
    out: list[Retrieved] = []
    taken: set[str] = set()
    expanded: set[str] = set()
    if config.pin_summary:
        for ref in index.pinned_refs:
            chunk = index.by_id[ref]
            taken.add(chunk.chunk_id)
            out.append(Retrieved(chunk, len(out) + 1, 0.0, "summary"))
    limit = len(out) + config.k

    def take(chunk: Chunk, score: float, source: Source) -> None:
        if chunk.chunk_id not in taken and len(out) < limit:
            taken.add(chunk.chunk_id)
            out.append(Retrieved(chunk, len(out) + 1, score, source))

    for chunk_id, score in ranked:
        if len(out) >= limit:
            break
        chunk = index.by_id[chunk_id]
        key = chunk.series_key
        if config.series_expansion <= 0 or key is None:
            take(chunk, score, "ranked")
            continue
        if key in expanded:
            continue  # the series already has its slots; keep room for other cards
        expanded.add(key)
        take(chunk, score, "ranked")
        for member in index.series[key][: config.series_expansion]:
            take(member, score, "series")
    return out
