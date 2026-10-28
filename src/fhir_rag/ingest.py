"""Build the SQLite index from the cohort: resources, cards, embeddings.

    python -m fhir_rag.ingest [--no-embed]

Rebuilding is cheap: records are rewritten, but embeddings are cached by card
text, so only changed cards are embedded again.
"""

import argparse
import hashlib
import logging
import sys
import time
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

from fhir_rag.config import get_settings
from fhir_rag.fhir.cards import CARD_VERSION, chunks_for
from fhir_rag.fhir.loader import (
    iter_resources,
    load_bundle,
    patient_bundle_paths,
    patient_of,
)
from fhir_rag.fhir.views import VIEW_TYPES, PatientView
from fhir_rag.retrieval.dense import Embedder
from fhir_rag.retrieval.summary import pinned_refs
from fhir_rag.store import PatientRow, Store

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class IngestStats:
    patients: int
    resources: int
    chunks: int
    embedded: int
    seconds: float


def cohort_hash(cohort_dir: Path) -> str:
    """SHA-256 of the cohort manifest: the version reports record (D15)."""
    manifest = cohort_dir / "MANIFEST.sha256"
    return hashlib.sha256(manifest.read_bytes()).hexdigest()[:12] if manifest.exists() else ""


def build_index(
    cohort_dir: Path,
    store: Store,
    embedder: Embedder | None,
    as_of: str,
    batch: int = 2048,
) -> IngestStats:
    started = time.monotonic()
    store.reset_records()
    n_resources = n_chunks = 0
    paths = patient_bundle_paths(cohort_dir)
    for path in paths:
        bundle = load_bundle(path)
        patient = PatientView.model_validate(patient_of(bundle))
        store.add_patient(
            PatientRow(patient.id, patient.display_name, patient.gender, patient.birth_date)
        )
        resources = [r for r in iter_resources(bundle) if r["resourceType"] in VIEW_TYPES]
        lookup = {r["id"]: r for r in iter_resources(bundle)}
        chunks = [c for r in resources for c in chunks_for(r, lookup)]
        store.add_resources(patient.id, resources)
        store.add_chunks(patient.id, chunks)
        store.add_pinned(patient.id, pinned_refs(resources, as_of))
        n_resources += len(resources)
        n_chunks += len(chunks)

    store.set_meta("cohort_hash", cohort_hash(cohort_dir))
    store.set_meta("card_version", CARD_VERSION)

    embedded = 0
    if embedder is not None:
        # Sorted by length so each batch pads to a similar size. In hash order
        # most batches hold one long note chunk and pad every short card to it;
        # measured on 2 threads, sorting cuts a full embed from ~48 to ~11 minutes.
        missing = sorted(store.missing_embeddings(embedder.model_name), key=lambda p: len(p[1]))
        for start in range(0, len(missing), batch):
            part = missing[start : start + batch]
            vectors = embedder.embed_documents([text for _, text in part])
            store.add_embeddings(embedder.model_name, [sha for sha, _ in part], vectors)
            embedded += len(part)
            log.info("embedded %d/%d cards", embedded, len(missing))
        store.prune_embeddings()
        store.set_meta("embedding_model", embedder.model_name)
    return IngestStats(len(paths), n_resources, n_chunks, embedded, time.monotonic() - started)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--no-embed", action="store_true", help="skip embeddings")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    settings = get_settings()
    embedder: Embedder | None = None
    if not args.no_embed:
        from fhir_rag.retrieval.dense import FastEmbedEmbedder

        embedder = FastEmbedEmbedder(settings.embedding_model)
    store = Store(settings.db_path)
    try:
        stats = build_index(settings.cohort_dir, store, embedder, settings.record_as_of)
    finally:
        store.close()
    print(
        f"{stats.patients} patients, {stats.resources} resources, {stats.chunks} cards, "
        f"{stats.embedded} newly embedded, {stats.seconds:.1f}s -> {settings.db_path}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
