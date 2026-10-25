import asyncio
import json
from pathlib import Path

from cohort import P1, P2, bundle, patient_one, patient_two

from fhir_rag.config import Settings
from fhir_rag.evals.build_questions import check_gold
from fhir_rag.evals.questions import Question, assign_splits
from fhir_rag.evals.report_answers import write_report
from fhir_rag.evals.run_answers import null_llm, oracle_llm, run
from fhir_rag.evals.templates import template_questions
from fhir_rag.llm.answer import AnswerService
from fhir_rag.llm.client import FakeLLM, LLMTimeout
from fhir_rag.retrieval.retriever import Retriever


def _by_slug(questions: list[Question]) -> dict[str, Question]:
    return {q.id.split(":")[0]: q for q in questions}


def test_templates_compute_gold_from_the_raw_record() -> None:
    qs = _by_slug(template_questions(P1, bundle(patient_one())))
    # P1 has two of the named labs, so both are asked about, each with its newest result.
    assert qs["latest-lab-4548-4"].gold_groups == [["Observation/p1-a1c-2026"]]
    assert qs["latest-lab-4548-4"].key_facts == ["6.8", "2026-03-04"]
    assert qs["latest-lab-2093-3"].gold_groups == [["Observation/p1-chol"]]
    assert qs["current-meds"].gold_groups == [["MedicationRequest/p1-lisinopril"]]
    assert qs["latest-bp"].key_facts == ["128", "82", "2026-06-01"]
    assert qs["a1c-trend"].gold_groups == [
        ["Observation/p1-a1c-2024"],
        ["Observation/p1-a1c-2025"],
        ["Observation/p1-a1c-2026"],
    ]
    assert qs["latest-lipid-panel"].gold_groups == [
        ["DiagnosticReport/p1-lipids", "Observation/p1-chol"]
    ]
    assert qs["prescribed-for-essential-hypertension"].gold_groups == [
        ["MedicationRequest/p1-lisinopril"]
    ]
    assert qs["never-colonoscopy"].gold_groups == []
    # The patient has hypertension, so "never had high blood pressure" isn't asked.
    assert "never-high-blood-pressure" not in qs


def test_gold_checks_catch_refs_from_another_record() -> None:
    q = Question(
        id="x:p2",
        patient_id=P2,
        question="?",
        category="fact_lookup",
        gold_groups=[["Observation/p1-a1c-2026"]],
        source="template",
    )
    refs = {P2: {"Observation/p2-a1c"}}
    assert check_gold([q], refs) == ["x:p2: Observation/p1-a1c-2026 is not in patient p2's record"]


def test_splits_are_stable_and_roughly_sixty_forty() -> None:
    qs = [
        Question(
            id=f"q{i}",
            patient_id=P1,
            question="?",
            category="fact_lookup",
            gold_groups=[["Condition/p1-htn"]],
            source="template",
        )
        for i in range(10)
    ]
    first = {q.id: q.split for q in assign_splits(qs)}
    again = {q.id: q.split for q in assign_splits(list(reversed(qs)))}
    assert first == again
    assert list(first.values()).count("dev") == 6


def _questions() -> list[Question]:
    qs = template_questions(P1, bundle(patient_one())) + template_questions(
        P2, bundle(patient_two())
    )
    return assign_splits(qs)


def test_oracle_and_null_bracket_the_metrics(
    tmp_path: Path, retriever: Retriever, settings: Settings
) -> None:
    questions = _questions()
    asyncio.run(
        run(
            questions,
            lambda q: AnswerService(retriever, oracle_llm(q), settings),
            None,
            settings,
            tmp_path / "oracle",
            1,
            4,
            100.0,
            None,
        )
    )
    null_service = AnswerService(retriever, null_llm(), settings)
    asyncio.run(
        run(questions, lambda q: null_service, None, settings, tmp_path / "null", 1, 4, 100.0, None)
    )

    def mean(run_name: str, key: str) -> float:
        rows = [json.loads(line) for line in (tmp_path / run_name / "results.jsonl").open()]
        values = [r["scores"][key] for r in rows if r["scores"].get(key) is not None]
        return sum(values) / len(values)

    assert mean("oracle", "key_facts") == 1.0
    assert mean("oracle", "citation_precision") > 0.9
    assert mean("null", "citation_recall") == 0.0
    assert mean("null", "key_facts") == 0.0
    report = write_report(tmp_path / "oracle", tmp_path / "oracle.md").read_text()
    assert "## Abstention" in report


def test_failed_attempts_go_to_errors_and_resume_retries_them(
    tmp_path: Path, retriever: Retriever, settings: Settings
) -> None:
    questions = _questions()[:3]
    failing = AnswerService(retriever, FakeLLM(lambda s, u, t: LLMTimeout("slow")), settings)
    asyncio.run(
        run(questions, lambda q: failing, None, settings, tmp_path / "r", 1, 2, 100.0, None)
    )
    assert not (tmp_path / "r" / "results.jsonl").exists()
    errors = [json.loads(line) for line in (tmp_path / "r" / "errors.jsonl").open()]
    assert {e["kind"] for e in errors} == {"timeout"} and len(errors) == 3

    working = AnswerService(retriever, null_llm(), settings)
    asyncio.run(
        run(questions, lambda q: working, None, settings, tmp_path / "r", 1, 2, 100.0, None)
    )
    asyncio.run(
        run(questions, lambda q: working, None, settings, tmp_path / "r", 1, 2, 100.0, None)
    )
    rows = (tmp_path / "r" / "results.jsonl").read_text().splitlines()
    assert len(rows) == 3  # the second pass resumed and found nothing left to do
