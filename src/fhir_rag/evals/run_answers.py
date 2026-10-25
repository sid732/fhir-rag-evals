"""Answer eval: runs the real answer pipeline on labeled questions (PLAN.md D13-D15).

    python -m fhir_rag.evals.run_answers --run NAME [--split dev] [--limit N]
        [--reps 1] [--concurrency 4] [--spend-cap 10] [--no-judge]
        [--mode real|oracle|null]

Each (question, repetition) becomes one line in evals/runs/NAME/results.jsonl,
written as soon as it finishes; rerunning the same NAME resumes where it
stopped. Attempts that fail before producing a gradable answer (timeouts, API
errors, refusals, unparseable output) go to errors.jsonl with a failure class
and are never scored as wrong answers. A run stops starting new questions
once the recorded cost reaches --spend-cap dollars.

--mode oracle answers from the gold labels and --mode null answers "I don't
know" with no citations. Neither calls the API (unless the judge is on), and
together they test the harness: oracle should score near the top and null
near zero. evals/reports/answers-NAME.md summarizes a run.
"""

import argparse
import asyncio
import json
import sys
import time
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import Any

from fhir_rag.config import Settings, get_settings
from fhir_rag.evals.common import git_version
from fhir_rag.evals.judge import judge_answer
from fhir_rag.evals.metrics import (
    citation_scores,
    dates_in,
    key_facts_present,
    numbers_in,
    resource_of,
    unsupported_numbers_and_dates,
)
from fhir_rag.evals.questions import Question, Split, load_questions
from fhir_rag.evals.report_answers import write_report
from fhir_rag.llm.answer import AnswerResult, AnswerService
from fhir_rag.llm.client import AnthropicLLM, FakeLLM, LLMClient, LLMError
from fhir_rag.retrieval.dense import Embedder
from fhir_rag.retrieval.retriever import Retriever
from fhir_rag.store import Store

QUESTIONS = Path("evals/questions/questions.jsonl")
RUNS = Path("evals/runs")
CASE_TIMEOUT_S = 240.0


def oracle_llm(q: Question) -> FakeLLM:
    """Answers built from one question's gold labels: what a perfect model would say."""

    def respond(system: str, user: str, schema: type[Any]) -> dict[str, Any]:
        if not q.answerable:
            return {
                "status": "not_in_record",
                "sentences": [{"text": "The record has no such entry.", "citations": []}],
            }
        cited = [ref for group in q.gold_groups for ref in group]
        facts = ", ".join(q.key_facts) or "see cited records"
        return {
            "status": "answered",
            "sentences": [{"text": f"Recorded: {facts}.", "citations": cited}],
        }

    return FakeLLM(respond, model="oracle")


def null_llm() -> FakeLLM:
    def respond(system: str, user: str, schema: type[Any]) -> dict[str, Any]:
        return {
            "status": "answered",
            "sentences": [{"text": "I don't know.", "citations": []}],
        }

    return FakeLLM(respond, model="null")


def score_case(q: Question, result: AnswerResult) -> dict[str, Any]:
    """Deterministic metrics for one answer (the judge's are added separately)."""
    answer = result.answer
    retrieved_ids = [r.chunk.chunk_id for r in result.retrieved]
    cards = {r.chunk.chunk_id: r.chunk.text for r in result.retrieved}
    cards |= {r.chunk.resource_ref: r.chunk.text for r in result.retrieved}
    abstained = answer.status == "not_in_record"
    scores: dict[str, Any] = {"abstained": abstained, "answerable": q.answerable}
    if q.answerable and not abstained:
        cs = citation_scores(answer.raw_citations, retrieved_ids, q.gold_groups)
        scores |= {
            "citation_validity": cs.validity,
            "citation_precision": cs.precision,
            "citation_recall": cs.recall,
            "key_facts": key_facts_present(answer.text, q.key_facts) if q.key_facts else None,
        }
        # Of the sentences that state a number or date, the share whose numbers
        # and dates all appear in the cards they cite. None if no sentence has one,
        # so answers without numbers can't pass the check vacuously.
        checks = [
            not unsupported_numbers_and_dates(s.text, [cards[c] for c in s.citations if c in cards])
            for s in answer.sentences
            if numbers_in(s.text) or dates_in(s.text)
        ]
        scores["numbers_dates_ok"] = sum(checks) / len(checks) if checks else None
        scores["context_has_gold"] = any(
            resource_of(c) in set(g) for g in q.gold_groups for c in retrieved_ids
        )
    return scores


async def run_case(
    q: Question,
    rep: int,
    service: AnswerService,
    judge: LLMClient | None,
    settings: Settings,
) -> dict[str, Any]:
    result = await service.answer(q.patient_id, q.question)
    row: dict[str, Any] = {
        "question_id": q.id,
        "rep": rep,
        "patient_id": q.patient_id,
        "category": q.category,
        "question": q.question,
        "status": result.answer.status,
        "answer": [
            {"text": s.text, "citations": s.citations, "invalid": s.invalid}
            for s in result.answer.sentences
        ],
        "retrieved": [[r.chunk.chunk_id, r.source] for r in result.retrieved],
        "gold_groups": q.gold_groups,
        "key_facts": q.key_facts,
        "model": result.model,
        "usage": result.usage.__dict__,
        "cost_usd": result.cost_usd,
        "latency_s": {
            "retrieval": result.retrieval_s,
            "llm": result.llm_s,
            "total": result.total_s,
        },
        "prompt_version": result.prompt_version,
        "scores": score_case(q, result),
    }
    if judge is not None and result.answer.status == "answered" and result.answer.sentences:
        cards = {r.chunk.chunk_id: r.chunk.text for r in result.retrieved}
        cards |= {r.chunk.resource_ref: r.chunk.text for r in result.retrieved}
        verdict = await judge_answer(judge, settings, q.question, result.answer, cards)
        row["judge"] = {
            "verdicts": verdict.verdicts,
            "reasons": verdict.reasons,
            "model": verdict.model,
            "usage": verdict.usage.__dict__,
            "cost_usd": verdict.cost_usd,
        }
        if verdict.verdicts:
            n = len(verdict.verdicts)
            row["scores"]["faithfulness"] = verdict.verdicts.count("supported") / n
            row["scores"]["partially_supported"] = verdict.verdicts.count("partially_supported") / n
    return row


def _done(path: Path) -> set[tuple[str, int]]:
    if not path.exists():
        return set()
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    return {(r["question_id"], r["rep"]) for r in rows}


def _row_cost(row: dict[str, Any]) -> float:
    total = row.get("cost_usd") or 0.0
    return float(total + ((row.get("judge") or {}).get("cost_usd") or 0.0))


async def run(
    questions: Sequence[Question],
    service_for: Callable[[Question], AnswerService],
    judge: LLMClient | None,
    settings: Settings,
    out_dir: Path,
    reps: int,
    concurrency: int,
    spend_cap: float,
    requested_model: str | None,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    results_path, errors_path = out_dir / "results.jsonl", out_dir / "errors.jsonl"
    done = _done(results_path)
    spent = sum(
        _row_cost(json.loads(line))
        for line in (results_path.read_text().splitlines() if results_path.exists() else [])
        if line.strip()
    )
    pending = [(q, rep) for rep in range(reps) for q in questions if (q.id, rep) not in done]
    semaphore = asyncio.Semaphore(concurrency)
    lock = asyncio.Lock()
    stop = asyncio.Event()

    async def one(q: Question, rep: int) -> None:
        nonlocal spent
        async with semaphore:
            if stop.is_set():
                return
            started = time.monotonic()
            try:
                row = await asyncio.wait_for(
                    run_case(q, rep, service_for(q), judge, settings), CASE_TIMEOUT_S
                )
            except (LLMError, TimeoutError) as e:
                kind = e.kind if isinstance(e, LLMError) else "case_timeout"
                error = {
                    "question_id": q.id,
                    "rep": rep,
                    "kind": kind,
                    "error": str(e)[:500],
                    "seconds": round(time.monotonic() - started, 1),
                }
                async with lock:
                    with errors_path.open("a") as f:
                        f.write(json.dumps(error) + "\n")
                return
            if requested_model and row["model"] != requested_model:
                row["served_model_mismatch"] = True  # a refusal fallback answered instead
            async with lock:
                with results_path.open("a") as f:
                    f.write(json.dumps(row) + "\n")
                spent += _row_cost(row)
                if spent >= spend_cap:
                    stop.set()

    await asyncio.gather(*(one(q, rep) for q, rep in pending))
    if stop.is_set():
        print(
            f"stopped at the spend cap: ${spent:.2f} >= ${spend_cap:.2f}",
            file=sys.stderr,
        )


def main(argv: Sequence[str] | None = None, embedder: Embedder | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--run", required=True, help="run name; results go to evals/runs/NAME")
    parser.add_argument("--split", choices=["dev", "test", "all"], default="dev")
    parser.add_argument("--limit", type=int, default=None, help="first N questions only")
    parser.add_argument("--reps", type=int, default=1)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--spend-cap", type=float, default=10.0, help="dollars")
    parser.add_argument("--no-judge", action="store_true")
    parser.add_argument("--mode", choices=["real", "oracle", "null"], default="real")
    args = parser.parse_args(argv)

    settings = get_settings()
    split: Split | None = None if args.split == "all" else args.split
    questions = load_questions(QUESTIONS, split)[: args.limit]
    key = settings.anthropic_api_key.get_secret_value() if settings.anthropic_api_key else None
    needs_api = args.mode == "real" or not args.no_judge
    if needs_api and key is None:
        print(
            "ANTHROPIC_API_KEY is not set; use --mode oracle|null with --no-judge",
            file=sys.stderr,
        )
        return 2
    real = AnthropicLLM(key, settings.llm_timeout_s, settings.llm_max_retries) if key else None
    if embedder is None:
        from fhir_rag.retrieval.dense import FastEmbedEmbedder

        embedder = FastEmbedEmbedder(settings.embedding_model)
    store = Store(settings.db_path)
    retriever = Retriever(store, embedder)
    service_for: Callable[[Question], AnswerService]
    if args.mode == "oracle":
        service_for = lambda q: AnswerService(retriever, oracle_llm(q), settings)  # noqa: E731
    elif args.mode == "null":
        null_service = AnswerService(retriever, null_llm(), settings)
        service_for = lambda q: null_service  # noqa: E731
    else:
        assert real is not None
        real_service = AnswerService(retriever, real, settings)
        service_for = lambda q: real_service  # noqa: E731
    out_dir = RUNS / args.run
    meta = {
        "commit": git_version(),
        "cohort": store.meta("cohort_hash") or "",
        "mode": args.mode,
        "generator": settings.generator_model if args.mode == "real" else args.mode,
        "effort": settings.generator_effort,
        "judge": None if args.no_judge else settings.judge_model,
        "retrieval": f"{settings.retrieval_mode}, k={settings.top_k}, "
        f"series={settings.series_expansion}, summary={settings.pin_summary}",
        "split": args.split,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    asyncio.run(
        run(
            questions,
            service_for,
            None if args.no_judge else real,
            settings,
            out_dir,
            args.reps,
            args.concurrency,
            args.spend_cap,
            settings.generator_model if args.mode == "real" else None,
        )
    )
    report = write_report(out_dir, Path("evals/reports") / f"answers-{args.run}.md")
    print(f"wrote {report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
