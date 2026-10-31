"""Faithfulness judge (PLAN.md D14): is each answer sentence supported by the record?

A separate Claude call (claude-sonnet-5-5 by default, a different model from
the generator) grades every answer sentence. Claims about specific entries
(values, dates, statuses) are checked against the cards that sentence cites.
Claims about the record as a whole ("most recent", "only", counts, "no record
of") are checked against the whole context the generator saw, since no single
cited card can show that nothing later or nothing else exists. One call per
answer, structured output.

Version 1 judged every sentence against its cited cards alone and marked most
"most recent" claims as unverifiable. Version 2 fixed that but graded each
sentence apart from the rest of its answer and guessed about entries it wasn't
shown. Version 3 reads each sentence within its answer and writes its reason
before its verdict. docs/evals.md has the comparisons.

Its numbers only count after calibration against hand labels
(fhir_rag.evals.calibrate).
"""

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel

from fhir_rag.config import Settings
from fhir_rag.llm.answer import CheckedAnswer, CheckedSentence, render_context
from fhir_rag.llm.client import LLMClient, Usage
from fhir_rag.llm.pricing import cost_usd
from fhir_rag.retrieval.retriever import Retrieved

type Verdict = Literal["supported", "partially_supported", "not_supported"]

JUDGE_PROMPT_FILE = Path(__file__).parent / "prompts" / "judge_v3.txt"
JUDGE_SYSTEM = JUDGE_PROMPT_FILE.read_text()
JUDGE_VERSION = f"{JUDGE_PROMPT_FILE.stem}-{hashlib.sha256(JUDGE_SYSTEM.encode()).hexdigest()[:8]}"


class SentenceVerdict(BaseModel):
    index: int
    reason: str  # before the verdict, so the verdict is generated after the reasoning
    verdict: Verdict


class JudgeOutput(BaseModel):
    verdicts: list[SentenceVerdict]


@dataclass(frozen=True)
class JudgeResult:
    verdicts: list[Verdict]  # one per answer sentence, in order
    reasons: list[str]
    model: str | None  # None when no call was needed
    usage: Usage
    cost_usd: float | None
    prompt_version: str = JUDGE_VERSION

    def as_row(self) -> dict[str, Any]:
        return {
            "verdicts": self.verdicts,
            "reasons": self.reasons,
            "model": self.model,
            "usage": self.usage.__dict__,
            "cost_usd": self.cost_usd,
            "prompt_version": self.prompt_version,
        }

    def scores(self) -> dict[str, float]:
        if not self.verdicts:
            return {}
        n = len(self.verdicts)
        return {
            "faithfulness": self.verdicts.count("supported") / n,
            "partially_supported": self.verdicts.count("partially_supported") / n,
        }


def cited_excerpts(citation: str, retrieved: list[Retrieved]) -> list[str]:
    """Cards a citation names: one card, or every card of a resource (note chunks)."""
    return [r.chunk.text for r in retrieved if citation in (r.chunk.chunk_id, r.chunk.resource_ref)]


def judge_prompt(
    question: str, sentences: list[CheckedSentence], retrieved: list[Retrieved], as_of: str
) -> str:
    parts = [render_context(retrieved, as_of), "", f"Question asked: {question}", ""]
    parts += ["Answer: " + " ".join(s.text for s in sentences), ""]
    for index, sentence in enumerate(sentences):
        parts.append(f"Sentence {index}: {sentence.text}")
        cited = [
            f"  cited [{c}]: {text}"
            for c in sentence.citations
            for text in cited_excerpts(c, retrieved)
        ]
        parts += cited or ["  cites nothing"]
        parts.append("")
    return "\n".join(parts).rstrip()


async def judge_answer(
    llm: LLMClient,
    settings: Settings,
    question: str,
    answer: CheckedAnswer,
    retrieved: list[Retrieved],
) -> JudgeResult:
    """Grade every sentence of an answer against the context it was written from."""
    n = len(answer.sentences)
    if n == 0:
        return JudgeResult([], [], None, Usage(), 0.0)
    result = await llm.parse(
        model=settings.judge_model,
        system=JUDGE_SYSTEM,
        user=judge_prompt(question, answer.sentences, retrieved, settings.record_as_of),
        schema=JudgeOutput,
        effort=settings.judge_effort,
        max_tokens=settings.max_output_tokens,
    )
    by_index = {v.index: v for v in result.parsed.verdicts}
    verdicts: list[Verdict] = []
    reasons: list[str] = []
    for i in range(n):
        if i in by_index:
            verdicts.append(by_index[i].verdict)
            reasons.append(by_index[i].reason)
        else:  # a missing verdict counts against the answer, and says so
            verdicts.append("not_supported")
            reasons.append("judge returned no verdict for this sentence")
    return JudgeResult(
        verdicts, reasons, result.model, result.usage, cost_usd(result.model, result.usage)
    )
