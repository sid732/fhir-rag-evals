import pytest

from fhir_rag.evals.calibrate import cohen_kappa
from fhir_rag.evals.metrics import (
    Abstention,
    bootstrap_ci,
    citation_scores,
    hit_at_k,
    key_facts_present,
    mrr_at_k,
    recall_at_k,
    unsupported_numbers_and_dates,
)
from fhir_rag.evals.run_retrieval import check_baseline

GOLD = [["Observation/a", "Observation/a2"], ["Condition/b"]]


def test_retrieval_metrics_count_groups() -> None:
    ranked = ["Encounter/x", "Observation/a2", "DocumentReference/n#1", "Condition/b"]
    assert hit_at_k(ranked, GOLD, 1) == 0.0
    assert hit_at_k(ranked, GOLD, 2) == 1.0
    assert recall_at_k(ranked, GOLD, 2) == 0.5  # one of two groups
    assert recall_at_k(ranked, GOLD, 4) == 1.0
    assert mrr_at_k(ranked, GOLD, 4) == 0.5  # first gold at rank 2
    assert recall_at_k(ranked, [], 4) == 0.0


def test_note_chunks_count_as_their_resource() -> None:
    gold = [["DocumentReference/n"]]
    assert hit_at_k(["DocumentReference/n#2"], gold, 1) == 1.0


def test_citation_scores_separate_validity_from_precision() -> None:
    retrieved = ["Observation/a", "Encounter/x", "DocumentReference/n#1"]
    scores = citation_scores(["Observation/a", "Encounter/x", "Made/up"], retrieved, GOLD)
    assert scores.validity == pytest.approx(2 / 3)
    assert scores.precision == 0.5  # of the two valid citations, one is gold
    assert scores.recall == 0.5
    assert citation_scores(["DocumentReference/n"], retrieved, GOLD).validity == 1.0
    assert citation_scores([], retrieved, GOLD).validity is None


def test_numbers_and_dates_must_appear_in_cited_cards() -> None:
    card = "Observation | 2026-03-04 | Hemoglobin A1c = 6.8 % | LOINC 4548-4"
    ok = "The most recent HbA1c was 6.8% on 2026-03-04."
    assert unsupported_numbers_and_dates(ok, [card]) == []
    bad = "The most recent HbA1c was 6.9% on 2026-03-05."
    assert unsupported_numbers_and_dates(bad, [card]) == ["2026-03-05", "6.9"]


def test_key_facts_compare_numbers_as_numbers() -> None:
    assert key_facts_present("A1c 6.80 on 2026-03-04", ["6.8", "2026-03-04"]) == 1.0
    assert key_facts_present("A1c 6.8", ["6.8", "2026-03-04"]) == 0.5
    assert key_facts_present("anything", []) == 1.0


def test_abstention_matrix() -> None:
    m = Abstention().add(True, False).add(False, True).add(False, False).add(True, True)
    assert m.abstain_precision == 0.5 and m.abstain_recall == 0.5


def test_cluster_bootstrap_brackets_the_mean() -> None:
    values = [1.0, 1.0, 0.0, 0.0, 1.0, 0.0]
    clusters = ["p1", "p1", "p2", "p2", "p3", "p3"]
    ci = bootstrap_ci(values, clusters, reps=500)
    assert ci.low <= ci.mean == 0.5 <= ci.high
    assert bootstrap_ci([], []).n == 0


def test_cohen_kappa() -> None:
    assert cohen_kappa(["a", "b", "a", "b"], ["a", "b", "a", "b"]) == 1.0
    assert cohen_kappa(["a", "a", "b", "b"], ["a", "b", "a", "b"]) == 0.0


def test_baseline_check_allows_one_question_of_noise() -> None:
    baseline = {"headline": {"recall@10": 0.90}, "answerable": 100, "leaks": 0}
    assert check_baseline({**baseline, "headline": {"recall@10": 0.89}}, baseline) == []
    assert check_baseline({**baseline, "headline": {"recall@10": 0.85}}, baseline)
    assert check_baseline({**baseline, "leaks": 1}, baseline)
