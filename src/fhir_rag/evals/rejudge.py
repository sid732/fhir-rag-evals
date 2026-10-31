"""Re-grade a finished answer run with the current judge, without new answers.

    python -m fhir_rag.evals.rejudge --from NAME --run NEW [--concurrency 4] [--spend-cap 3]

Reads evals/runs/NAME/results.jsonl and writes evals/runs/NEW with the same
answers and fresh judge verdicts. The judge sees the context the generator
saw, rebuilt from the index by card id, so the index must hold the cohort and
card version the source run used. Rows that were never judged (abstentions)
are copied as they are, so the report still covers every case. As in
run_answers, rows are written as they finish, a rerun resumes, failed judge
calls go to errors.jsonl, and no new call starts once judge spending reaches
--spend-cap dollars.
"""

import argparse
import asyncio
import json
import sys
import time
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from fhir_rag.config import Settings, get_settings
from fhir_rag.evals.common import git_version
from fhir_rag.evals.judge import JUDGE_VERSION, judge_answer
from fhir_rag.evals.report_answers import write_report
from fhir_rag.evals.run_answers import CASE_TIMEOUT_S, RUNS, done_cases
from fhir_rag.fhir.cards import Chunk
from fhir_rag.llm.answer import CheckedAnswer, CheckedSentence
from fhir_rag.llm.client import AnthropicLLM, LLMClient, LLMError
from fhir_rag.retrieval.retriever import Retrieved
from fhir_rag.store import Store

JUDGE_SCORES = ("faithfulness", "partially_supported")


def rebuild_context(row: dict[str, Any], chunks: dict[str, Chunk]) -> list[Retrieved]:
    """The cards the generator saw, in its order. Scores aren't shown to any model."""
    return [
        Retrieved(chunks[chunk_id], rank, 0.0, source)
        for rank, (chunk_id, source) in enumerate(row["retrieved"], start=1)
    ]


def answer_of(row: dict[str, Any]) -> CheckedAnswer:
    sentences = [CheckedSentence(s["text"], s["citations"], s["invalid"]) for s in row["answer"]]
    return CheckedAnswer(row["status"], sentences)


async def rejudge_row(
    row: dict[str, Any], judge: LLMClient, settings: Settings, chunks: dict[str, Chunk]
) -> dict[str, Any]:
    scores = {k: v for k, v in row["scores"].items() if k not in JUDGE_SCORES}
    new = {k: v for k, v in row.items() if k != "judge"} | {"scores": scores}
    if row["status"] != "answered" or not row["answer"]:
        return new
    verdict = await judge_answer(
        judge, settings, row["question"], answer_of(row), rebuild_context(row, chunks)
    )
    new["judge"] = verdict.as_row()
    new["scores"] |= verdict.scores()
    return new


def _judge_cost(row: dict[str, Any]) -> float:
    return float((row.get("judge") or {}).get("cost_usd") or 0.0)


async def rejudge(
    rows: Sequence[dict[str, Any]],
    judge: LLMClient,
    settings: Settings,
    chunks: dict[str, dict[str, Chunk]],
    out_dir: Path,
    concurrency: int,
    spend_cap: float,
) -> None:
    """chunks maps patient id -> chunk id -> card."""
    out_dir.mkdir(parents=True, exist_ok=True)
    results_path, errors_path = out_dir / "results.jsonl", out_dir / "errors.jsonl"
    done = done_cases(results_path)
    spent = sum(
        _judge_cost(json.loads(line))
        for line in (results_path.read_text().splitlines() if results_path.exists() else [])
        if line.strip()
    )
    pending = [r for r in rows if (r["question_id"], r["rep"]) not in done]
    semaphore = asyncio.Semaphore(concurrency)
    lock = asyncio.Lock()
    stop = asyncio.Event()

    async def one(row: dict[str, Any]) -> None:
        nonlocal spent
        async with semaphore:
            if stop.is_set():
                return
            started = time.monotonic()
            try:
                new = await asyncio.wait_for(
                    rejudge_row(row, judge, settings, chunks[row["patient_id"]]), CASE_TIMEOUT_S
                )
            except (LLMError, TimeoutError) as e:
                error = {
                    "question_id": row["question_id"],
                    "rep": row["rep"],
                    "kind": e.kind if isinstance(e, LLMError) else "case_timeout",
                    "error": str(e)[:500],
                    "seconds": round(time.monotonic() - started, 1),
                }
                async with lock:
                    with errors_path.open("a") as f:
                        f.write(json.dumps(error) + "\n")
                return
            async with lock:
                with results_path.open("a") as f:
                    f.write(json.dumps(new) + "\n")
                spent += _judge_cost(new)
                if spent >= spend_cap:
                    stop.set()

    await asyncio.gather(*(one(r) for r in pending))
    if stop.is_set():
        print(f"stopped at the spend cap: ${spent:.2f} >= ${spend_cap:.2f}", file=sys.stderr)


def load_chunks(store: Store, rows: Sequence[dict[str, Any]]) -> dict[str, dict[str, Chunk]]:
    """Cards for every patient in the run. Raises KeyError if a retrieved card is gone."""
    chunks: dict[str, dict[str, Chunk]] = {}
    for row in rows:
        pid = row["patient_id"]
        if pid not in chunks:
            chunks[pid] = {c.chunk_id: c for c in store.chunks(pid)}
        missing = [cid for cid, _ in row["retrieved"] if cid not in chunks[pid]]
        if missing:
            raise KeyError(f"{row['question_id']}: {len(missing)} cards not in the index")
    return chunks


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--from", dest="source", required=True, help="run to re-grade")
    parser.add_argument("--run", required=True, help="new run name; goes to evals/runs/NAME")
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--spend-cap", type=float, default=3.0, help="dollars of judge calls")
    args = parser.parse_args(argv)

    settings = get_settings()
    if settings.anthropic_api_key is None:
        print("ANTHROPIC_API_KEY is not set", file=sys.stderr)
        return 2
    source = RUNS / args.source
    rows = [json.loads(line) for line in (source / "results.jsonl").open() if line.strip()]
    meta = json.loads((source / "meta.json").read_text())
    store = Store(settings.db_path)
    try:
        index = {"cohort": store.meta("cohort_hash"), "card_version": store.meta("card_version")}
        stale = [k for k, v in index.items() if meta.get(k, v) != v]
        if stale:
            print(f"the index doesn't match {args.source}: {', '.join(stale)}", file=sys.stderr)
            return 2
        chunks = load_chunks(store, rows)
    except KeyError as e:
        print(f"the index doesn't match {args.source}: {e}", file=sys.stderr)
        return 2
    finally:
        store.close()

    out_dir = RUNS / args.run
    out_dir.mkdir(parents=True, exist_ok=True)
    meta |= {
        "commit": git_version(),
        "answers_from": args.source,
        "judge": settings.judge_model,
        "judge_prompt": JUDGE_VERSION,
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    key = settings.anthropic_api_key.get_secret_value()
    judge = AnthropicLLM(key, settings.llm_timeout_s, settings.llm_max_retries)
    asyncio.run(rejudge(rows, judge, settings, chunks, out_dir, args.concurrency, args.spend_cap))
    report = write_report(out_dir, Path("evals/reports") / f"answers-{args.run}.md")
    print(f"wrote {report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
