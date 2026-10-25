"""Answer a question: retrieve, call Claude with a schema, check every citation.

PLAN.md D10 and D11. The model returns sentences, each with the ids of the
excerpts it relies on, or status "not_in_record". Code then checks each
citation against what was actually retrieved: citations to anything else are
removed from the answer and reported, never shown as evidence.
"""

import asyncio
import hashlib
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

from fhir_rag.config import Settings
from fhir_rag.llm.client import LLMClient, Usage
from fhir_rag.llm.pricing import cost_usd
from fhir_rag.retrieval.retriever import RetrievalConfig, Retrieved, Retriever

PROMPT_FILE = Path(__file__).parent / "prompts" / "answer_v1.txt"
SYSTEM_PROMPT = PROMPT_FILE.read_text()
PROMPT_VERSION = f"answer_v1-{hashlib.sha256(SYSTEM_PROMPT.encode()).hexdigest()[:8]}"


class AnswerSentence(BaseModel):
    text: str
    citations: list[str] = Field(description="ids of the excerpts that support this sentence")


class AnswerOutput(BaseModel):
    status: Literal["answered", "not_in_record"]
    sentences: list[AnswerSentence]


def render_context(retrieved: list[Retrieved], as_of: str) -> str:
    summary = [r for r in retrieved if r.source == "summary"]
    ranked = [r for r in retrieved if r.source != "summary"]
    lines = [f'<record as_of="{as_of}">']
    if summary:
        lines.append("Patient summary (included with every question):")
        lines += [f"[{r.chunk.chunk_id}] {r.chunk.text}" for r in summary]
    lines.append("Retrieved for this question:")
    lines += [f"[{r.chunk.chunk_id}] {r.chunk.text}" for r in ranked] or ["(nothing matched)"]
    lines.append("</record>")
    return "\n".join(lines)


def user_message(question: str, retrieved: list[Retrieved], as_of: str) -> str:
    return f"{render_context(retrieved, as_of)}\n\nQuestion: {question}"


@dataclass(frozen=True)
class CheckedSentence:
    text: str
    citations: list[str]  # valid citations only, in the model's order
    invalid: list[str]  # cited ids that weren't in the context


@dataclass(frozen=True)
class CheckedAnswer:
    status: Literal["answered", "not_in_record"]
    sentences: list[CheckedSentence]

    @property
    def text(self) -> str:
        return " ".join(s.text for s in self.sentences)

    @property
    def raw_citations(self) -> list[str]:
        return [c for s in self.sentences for c in [*s.citations, *s.invalid]]

    @property
    def invalid_citations(self) -> list[str]:
        return [c for s in self.sentences for c in s.invalid]


def _clean(citation: str) -> str:
    return citation.strip().strip("[]").strip()


def check_citations(output: AnswerOutput, retrieved: list[Retrieved]) -> CheckedAnswer:
    """Keep citations that name a retrieved card or the resource behind one."""
    allowed = {r.chunk.chunk_id for r in retrieved} | {r.chunk.resource_ref for r in retrieved}
    sentences = []
    for sentence in output.sentences:
        valid: list[str] = []
        invalid: list[str] = []
        for citation in map(_clean, sentence.citations):
            target = valid if citation in allowed else invalid
            if citation not in target:
                target.append(citation)
        sentences.append(CheckedSentence(sentence.text, valid, invalid))
    return CheckedAnswer(output.status, sentences)


@dataclass(frozen=True)
class AnswerResult:
    patient_id: str
    question: str
    answer: CheckedAnswer
    retrieved: list[Retrieved]
    model: str
    usage: Usage
    cost_usd: float | None
    retrieval_s: float
    llm_s: float
    total_s: float
    prompt_version: str = PROMPT_VERSION
    request_id: str | None = None


class AnswerService:
    def __init__(self, retriever: Retriever, llm: LLMClient, settings: Settings) -> None:
        self._retriever = retriever
        self._llm = llm
        self._settings = settings
        self.config = RetrievalConfig(
            mode=settings.retrieval_mode,
            k=settings.top_k,
            series_expansion=settings.series_expansion,
            pin_summary=settings.pin_summary,
        )

    async def answer(self, patient_id: str, question: str) -> AnswerResult:
        started = time.monotonic()
        # Embedding the query is CPU work; keep it off the event loop.
        retrieved = await asyncio.to_thread(
            self._retriever.retrieve, patient_id, question, self.config
        )
        after_retrieval = time.monotonic()
        result = await self._llm.parse(
            model=self._settings.generator_model,
            system=SYSTEM_PROMPT,
            user=user_message(question, retrieved, self._settings.record_as_of),
            schema=AnswerOutput,
            effort=self._settings.generator_effort,
            max_tokens=self._settings.max_output_tokens,
        )
        finished = time.monotonic()
        return AnswerResult(
            patient_id=patient_id,
            question=question,
            answer=check_citations(result.parsed, retrieved),
            retrieved=retrieved,
            model=result.model,
            usage=result.usage,
            cost_usd=cost_usd(result.model, result.usage),
            retrieval_s=after_retrieval - started,
            llm_s=finished - after_retrieval,
            total_s=finished - started,
            request_id=result.request_id,
        )
