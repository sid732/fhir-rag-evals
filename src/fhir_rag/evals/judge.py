"""Faithfulness judge (PLAN.md D14): is each sentence supported by what it cites?

A separate Claude call (claude-sonnet-5-5 by default, a different model from
the generator) grades every answer sentence against the cards that sentence
cites, and nothing else. One call per answer, structured output, a rubric of
checkable properties. Sentences with no valid citation are not_supported
without asking the judge.

Its numbers only count after calibration against hand labels
(fhir_rag.evals.calibrate).
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from pydantic import BaseModel

from fhir_rag.config import Settings
from fhir_rag.llm.answer import CheckedAnswer
from fhir_rag.llm.client import LLMClient, Usage
from fhir_rag.llm.pricing import cost_usd

type Verdict = Literal["supported", "partially_supported", "not_supported"]

JUDGE_PROMPT_FILE = Path(__file__).parent / "prompts" / "judge_v1.txt"
JUDGE_SYSTEM = JUDGE_PROMPT_FILE.read_text()


class SentenceVerdict(BaseModel):
    index: int
    verdict: Verdict
    reason: str


class JudgeOutput(BaseModel):
    verdicts: list[SentenceVerdict]


@dataclass(frozen=True)
class JudgeResult:
    verdicts: list[Verdict]  # one per answer sentence, in order
    reasons: list[str]
    model: str | None  # None when no call was needed
    usage: Usage
    cost_usd: float | None


def judge_prompt(question: str, sentences: list[tuple[int, str, list[str]]]) -> str:
    parts = [f"Question asked: {question}", ""]
    for index, text, evidence in sentences:
        parts.append(f"Sentence {index}: {text}")
        parts += [f"  cited excerpt: {e}" for e in evidence]
        parts.append("")
    return "\n".join(parts).rstrip()


async def judge_answer(
    llm: LLMClient,
    settings: Settings,
    question: str,
    answer: CheckedAnswer,
    card_text: dict[str, str],
) -> JudgeResult:
    """Grade every sentence of an answer. card_text maps card ids and refs to text."""
    verdicts: dict[int, Verdict] = {}
    reasons: dict[int, str] = {}
    to_judge = []
    for i, sentence in enumerate(answer.sentences):
        evidence = [card_text[c] for c in sentence.citations if c in card_text]
        if evidence:
            to_judge.append((i, sentence.text, evidence))
        else:
            verdicts[i] = "not_supported"
            reasons[i] = "cites no excerpt from the context"
    if not to_judge:
        return JudgeResult(
            [verdicts[i] for i in range(len(answer.sentences))],
            [reasons[i] for i in range(len(answer.sentences))],
            None,
            Usage(),
            0.0,
        )
    result = await llm.parse(
        model=settings.judge_model,
        system=JUDGE_SYSTEM,
        user=judge_prompt(question, to_judge),
        schema=JudgeOutput,
        effort=settings.judge_effort,
        max_tokens=settings.max_output_tokens,
    )
    by_index = {v.index: v for v in result.parsed.verdicts}
    for i, _, _ in to_judge:
        if i in by_index:
            verdicts[i] = by_index[i].verdict
            reasons[i] = by_index[i].reason
        else:  # a missing verdict counts against the answer, and says so
            verdicts[i] = "not_supported"
            reasons[i] = "judge returned no verdict for this sentence"
    n = len(answer.sentences)
    return JudgeResult(
        [verdicts[i] for i in range(n)],
        [reasons[i] for i in range(n)],
        result.model,
        result.usage,
        cost_usd(result.model, result.usage),
    )
