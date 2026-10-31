import json
from pathlib import Path

import pytest

from fhir_rag.evals import calibrate
from fhir_rag.evals.calibrate import Label, cohen_kappa, read_labels, stratified, summarize
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
    # Years count when a cited card has a date in that year; others don't.
    trend = "It was stable between 2026 and 2025."
    assert unsupported_numbers_and_dates(trend, [card, "Observation | 2025-01-09 | x"]) == []
    assert unsupported_numbers_and_dates("Unchanged since 2019.", [card]) == ["2019"]


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


def test_stratified_sample_keeps_the_flags_and_weights_each_stratum() -> None:
    items = [(f"s{i}", "supported") for i in range(20)]
    items += [("p1", "partially_supported"), ("n1", "not_supported")]
    picked = stratified(items, 6)
    weights = {key: weight for key, _, weight in picked}
    assert len(picked) == 6 and weights["p1"] == weights["n1"] == 1.0
    # The four passes sampled stand for all twenty.
    assert sum(w for _, verdict, w in picked if verdict == "supported") == 20


def test_labels_are_read_from_the_sheet_and_scored() -> None:
    sheet = "\n".join(
        [
            "## 1. `a#0#0`",
            "```text",
            "label: n",  # inside a card: ignored
            "```",
            "</details>",
            "label: s",
            "## 2. `b#0#0`",
            "</details>",
            "label: P?",
            "## 3. `c#0#0`",
            "</details>",
            "label: ",
        ]
    )
    labels = read_labels(sheet)
    assert labels == {
        "a#0#0": Label("supported", True),
        "b#0#0": Label("partially_supported", False),
    }
    verdicts = {k: {"judge": "supported", "weight": 2.0} for k in ("a#0#0", "b#0#0", "c#0#0")}
    lines = summarize(labels, verdicts)
    assert lines[0] == "2 of 3 sentences labeled, 1 marked unclear"
    assert lines[1] == "agreement 0.500 on the sample, 1.000 on clear cases"


def test_score_can_grade_a_later_judge_on_the_same_labels(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(calibrate, "LABELS_DIR", tmp_path / "labels")
    sheet, verdicts = calibrate.set_paths("set")
    sheet.parent.mkdir()
    sheet.write_text("## 1. `q#0#0`\n</details>\nlabel: s\n## 2. `q#0#1`\n</details>\nlabel: p\n")
    rows = [{"key": f"q#0#{i}", "judge": "partially_supported", "weight": 1.0} for i in (0, 1)]
    verdicts.write_text("".join(json.dumps(r) + "\n" for r in rows))
    run = tmp_path / "evals" / "runs" / "later"
    run.mkdir(parents=True)
    judged = {
        "question_id": "q",
        "rep": 0,
        "judge": {"verdicts": ["supported", "partially_supported"]},
    }
    (run / "results.jsonl").write_text(json.dumps(judged) + "\n")

    assert calibrate.score("set") == 0
    assert "agreement 0.500 on the sample" in capsys.readouterr().out
    assert calibrate.score("set", "later") == 0
    assert "agreement 1.000 on the sample" in capsys.readouterr().out


def test_baseline_check_allows_one_question_of_noise() -> None:
    baseline = {"headline": {"recall@10": 0.90}, "answerable": 100, "leaks": 0}
    assert check_baseline({**baseline, "headline": {"recall@10": 0.89}}, baseline) == []
    assert check_baseline({**baseline, "headline": {"recall@10": 0.85}}, baseline)
    assert check_baseline({**baseline, "leaks": 1}, baseline)
