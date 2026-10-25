from dataclasses import replace
from pathlib import Path

import pytest
from cohort import AS_OF, P1, P2, patient_one

from fhir_rag.ingest import build_index
from fhir_rag.retrieval.bm25 import BM25Index, tokenize
from fhir_rag.retrieval.dense import HashEmbedder
from fhir_rag.retrieval.fusion import rrf
from fhir_rag.retrieval.retriever import (
    RetrievalConfig,
    Retrieved,
    Retriever,
    UnknownPatientError,
)
from fhir_rag.retrieval.summary import pinned_refs
from fhir_rag.store import Store

PLAIN = RetrievalConfig(mode="bm25", k=5, series_expansion=0, pin_summary=False)


def test_tokenize_keeps_decimals_and_drops_stopwords() -> None:
    assert tokenize("What was the patient's HbA1c? It was 6.8 %") == ["s", "hba1c", "6.8"]


def test_bm25_prefers_rare_matching_terms() -> None:
    index = BM25Index(["a", "b", "c"], ["glucose test", "glucose glucose cholesterol", "weight"])
    scores = index.scores("cholesterol")
    assert scores[1] > 0 and scores[0] == 0 and scores[2] == 0
    assert index.scores("nothing matches").sum() == 0


def test_rrf_rewards_agreement_and_breaks_ties_by_id() -> None:
    fused = rrf([["x", "y"], ["y", "x"], ["y"]])
    assert [item for item, _ in fused] == ["y", "x"]
    assert [item for item, _ in rrf([["b"], ["a"]])] == ["a", "b"]  # equal scores


def test_pinned_summary_picks_current_items_and_recent_events() -> None:
    refs = pinned_refs(patient_one(), AS_OF)
    assert refs == [
        "Condition/p1-htn",  # active; the resolved sinusitis is left out
        "MedicationRequest/p1-lisinopril",  # active; the completed amoxicillin is left out
        "AllergyIntolerance/p1-allergy",
        "Encounter/p1-enc-2026",  # the three newest visits
        "Encounter/p1-enc-2025",
        "Encounter/p1-enc-2024",
        "Immunization/p1-flu-2026",  # within the last 12 months only
    ]


def test_retrieval_never_returns_another_patients_cards(retriever: Retriever, store: Store) -> None:
    for mode in ("bm25", "dense", "hybrid"):
        config = RetrievalConfig(mode=mode, k=40)  # type: ignore[arg-type]
        hits = retriever.retrieve(P2, "hemoglobin A1c hypertension lisinopril", config)
        assert hits
        assert {store.chunk_owner(h.chunk.chunk_id) for h in hits} == {P2}


def test_unknown_patient(retriever: Retriever) -> None:
    with pytest.raises(UnknownPatientError):
        retriever.retrieve("nobody", "anything", PLAIN)


def _a1c(hits: list[Retrieved]) -> list[tuple[str | None, str]]:
    return [(h.chunk.date, h.source) for h in hits if "4548-4" in h.chunk.text]


def test_identical_cards_tie_break_to_the_newest(retriever: Retriever) -> None:
    hits = retriever.retrieve(P1, "hemoglobin a1c", PLAIN)
    assert _a1c(hits) == [
        ("2026-03-04", "ranked"),
        ("2025-03-01", "ranked"),
        ("2024-03-01", "ranked"),
    ]


def test_series_expansion_adds_the_newest_results_after_an_old_match(
    retriever: Retriever,
) -> None:
    # "6.1" matches only the 2024 result; expansion adds the two newest.
    hits = retriever.retrieve(P1, "a1c 6.1", replace(PLAIN, series_expansion=2))
    assert _a1c(hits) == [
        ("2024-03-01", "ranked"),
        ("2026-03-04", "series"),
        ("2025-03-01", "series"),
    ]


def test_an_expanded_series_gets_no_more_slots(retriever: Retriever) -> None:
    hits = retriever.retrieve(P1, "hemoglobin a1c", replace(PLAIN, series_expansion=1))
    assert _a1c(hits) == [("2026-03-04", "ranked")]


def test_summary_comes_first_and_does_not_count_against_k(retriever: Retriever) -> None:
    hits = retriever.retrieve(P1, "cholesterol", replace(PLAIN, pin_summary=True, k=2))
    sources = [h.source for h in hits]
    n_summary = sources.count("summary")
    assert n_summary == 7
    assert sources[:n_summary] == ["summary"] * n_summary
    assert len(hits) == n_summary + 2
    assert [h.rank for h in hits] == list(range(1, len(hits) + 1))


def test_rebuilding_reuses_cached_embeddings(tmp_path: Path, cohort_dir: Path) -> None:
    store = Store(tmp_path / "again.sqlite")
    first = build_index(cohort_dir, store, HashEmbedder(), AS_OF)
    second = build_index(cohort_dir, store, HashEmbedder(), AS_OF)
    assert first.embedded == first.chunks > 0
    assert second.embedded == 0 and second.chunks == first.chunks
    assert store.resource("Claim/p1-claim") is None  # not indexed
    owner, resource = store.resource("Observation/p1-chol") or ("", {})
    assert owner == P1 and resource["valueQuantity"]["value"] == 190
    store.close()
