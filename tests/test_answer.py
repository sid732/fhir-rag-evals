import asyncio
from typing import Any

import pytest
from cohort import P1

from fhir_rag.config import Settings
from fhir_rag.evals.judge import judge_answer
from fhir_rag.llm.answer import (
    SYSTEM_PROMPT,
    AnswerOutput,
    AnswerService,
    CheckedAnswer,
    CheckedSentence,
    check_citations,
    user_message,
)
from fhir_rag.llm.client import FakeLLM, LLMTimeout, Usage
from fhir_rag.llm.pricing import cost_usd
from fhir_rag.retrieval.retriever import RetrievalConfig, Retriever


def _answer(status: str, *sentences: tuple[str, list[str]]) -> dict[str, Any]:
    return {"status": status, "sentences": [{"text": t, "citations": c} for t, c in sentences]}


def test_check_citations_keeps_only_cited_context(retriever: Retriever) -> None:
    retrieved = retriever.retrieve(P1, "a1c", RetrievalConfig(mode="bm25", k=3, pin_summary=False))
    real = retrieved[0].chunk.chunk_id
    output = AnswerOutput.model_validate(
        _answer("answered", ("HbA1c was 6.8 %.", [f"[{real}]", real, "Observation/invented"]))
    )
    checked = check_citations(output, retrieved)
    assert checked.sentences[0].citations == [real]  # brackets stripped, duplicate dropped
    assert checked.invalid_citations == ["Observation/invented"]
    assert checked.raw_citations == [real, "Observation/invented"]


def test_resource_refs_are_accepted_for_note_chunks(retriever: Retriever) -> None:
    retrieved = retriever.retrieve(
        P1, "headache plan", RetrievalConfig(mode="bm25", k=5, pin_summary=False)
    )
    assert any(r.chunk.chunk_id == "DocumentReference/p1-note#1" for r in retrieved)
    output = AnswerOutput.model_validate(
        _answer("answered", ("Headache.", ["DocumentReference/p1-note"]))
    )
    assert check_citations(output, retrieved).sentences[0].citations == [
        "DocumentReference/p1-note"
    ]


def test_prompt_marks_summary_and_record_date(retriever: Retriever) -> None:
    retrieved = retriever.retrieve(P1, "blood pressure", RetrievalConfig(mode="bm25", k=2))
    message = user_message("What is the BP?", retrieved, "2026-10-01")
    assert message.startswith('<record as_of="2026-10-01">')
    assert "Patient summary (included with every question):" in message
    assert "[Condition/p1-htn]" in message
    assert message.endswith("Question: What is the BP?")
    assert "not_in_record" in SYSTEM_PROMPT


def test_answer_service_end_to_end(retriever: Retriever, settings: Settings) -> None:
    def respond(system: str, user: str, schema: type[Any]) -> dict[str, Any]:
        assert "[Observation/p1-a1c-2026]" in user
        return _answer(
            "answered",
            ("The most recent HbA1c was 6.8 % on 2026-03-04.", ["Observation/p1-a1c-2026"]),
        )

    llm = FakeLLM(respond)
    result = asyncio.run(
        AnswerService(retriever, llm, settings).answer(P1, "most recent hemoglobin a1c")
    )
    assert result.answer.status == "answered"
    assert result.answer.sentences[0].citations == ["Observation/p1-a1c-2026"]
    assert result.model == "fake-model"
    assert result.total_s >= result.llm_s >= 0


def test_llm_errors_propagate(retriever: Retriever, settings: Settings) -> None:
    llm = FakeLLM(lambda s, u, schema: LLMTimeout("slow"))
    with pytest.raises(LLMTimeout):
        asyncio.run(AnswerService(retriever, llm, settings).answer(P1, "a1c"))


def test_cost_from_usage() -> None:
    usage = Usage(input_tokens=1_000_000, output_tokens=100_000, cache_read_input_tokens=1_000_000)
    assert cost_usd("claude-opus-5-5", usage) == pytest.approx(4.0 + 2.0 + 0.4)
    assert cost_usd("some-unlisted-model", usage) is None


def test_judge_sees_the_whole_context_and_every_sentence(
    retriever: Retriever, settings: Settings
) -> None:
    retrieved = retriever.retrieve(P1, "a1c", RetrievalConfig(mode="bm25", k=3))
    cited = retrieved[-1].chunk
    answer = CheckedAnswer(
        "answered",
        [
            CheckedSentence("Cited and supported.", [cited.resource_ref], []),
            CheckedSentence("No other entry is recorded.", [], []),
            CheckedSentence("Cited, but the judge skips it.", [cited.chunk_id], []),
        ],
    )

    def respond(system: str, user: str, schema: type[Any]) -> dict[str, Any]:
        # Every card the generator saw is in the prompt, not just the cited ones.
        assert all(f"[{r.chunk.chunk_id}] {r.chunk.text}" in user for r in retrieved)
        # A resource citation shows that resource's cards; an uncited sentence still goes.
        assert f"  cited [{cited.resource_ref}]: {cited.text}" in user
        assert "Sentence 1: No other entry is recorded.\n  cites nothing" in user
        return {
            "verdicts": [
                {"index": 0, "verdict": "supported", "reason": "stated"},
                {"index": 1, "verdict": "supported", "reason": "no other entry in the record"},
            ]
        }

    result = asyncio.run(judge_answer(FakeLLM(respond), settings, "q?", answer, retrieved))
    assert result.verdicts == ["supported", "supported", "not_supported"]
    assert "no verdict" in result.reasons[2]
    assert result.scores() == {"faithfulness": 2 / 3, "partially_supported": 0.0}
