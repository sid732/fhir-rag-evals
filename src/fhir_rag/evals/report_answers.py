"""Summarize an answer-eval run (evals/runs/NAME) as markdown.

Every number is recomputed from the per-case rows in results.jsonl. Means
carry 95% cluster-bootstrap intervals over patients. Cost and latency are
reported in absolute terms.
"""

import json
from pathlib import Path
from statistics import quantiles
from typing import Any

from fhir_rag.evals.common import table
from fhir_rag.evals.metrics import Abstention, bootstrap_ci
from fhir_rag.evals.questions import CATEGORIES

METRICS = [
    ("citation_validity", "Citation validity"),
    ("citation_precision", "Citation precision"),
    ("citation_recall", "Citation recall"),
    ("numbers_dates_ok", "Numbers and dates in cited cards"),
    ("key_facts", "Key facts present"),
    ("faithfulness", "Faithfulness (judge: supported)"),
    ("partially_supported", "Judge: partially supported"),
    ("context_has_gold", "Gold evidence in context"),
]


def _rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _pct(values: list[float], q: int) -> float:
    if len(values) < 2:
        return values[0] if values else 0.0
    return quantiles(values, n=100)[q - 1]


def write_report(run_dir: Path, out: Path) -> Path:
    rows = _rows(run_dir / "results.jsonl")
    errors = _rows(run_dir / "errors.jsonl")
    meta = (
        json.loads((run_dir / "meta.json").read_text()) if (run_dir / "meta.json").exists() else {}
    )
    lines = [
        f"# Answer eval: {run_dir.name}",
        "",
        ", ".join(f"{k}: `{v}`" for k, v in meta.items()),
        "",
        f"{len(rows)} graded cases, {len(errors)} failed attempts (not scored).",
    ]
    if errors:
        kinds: dict[str, int] = {}
        for e in errors:
            kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
        lines.append("Failures by kind: " + ", ".join(f"{k} {v}" for k, v in sorted(kinds.items())))
    mismatched = sum(1 for r in rows if r.get("served_model_mismatch"))
    if mismatched:
        lines.append(
            f"{mismatched} answers were served by a fallback model, not the one requested."
        )
    if not rows:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines) + "\n")
        return out

    matrix = Abstention()
    for r in rows:
        matrix = matrix.add(r["scores"]["answerable"], r["scores"]["abstained"])
    lines += [
        "",
        "## Abstention",
        "",
        *table(
            ["", "Answered", "Said not in record"],
            [
                ["Answerable", matrix.answered_answerable, matrix.abstained_answerable],
                [
                    "Not in record",
                    matrix.answered_unanswerable,
                    matrix.abstained_unanswerable,
                ],
            ],
        ),
        "",
        f"'Not in record' precision {matrix.abstain_precision:.3f}, "
        f"recall {matrix.abstain_recall:.3f}.",
    ]

    graded = [r for r in rows if r["scores"]["answerable"] and not r["scores"]["abstained"]]
    lines += ["", f"## Answered, answerable cases ({len(graded)})", ""]
    metric_rows = []
    for key, label in METRICS:
        pairs = [
            (float(r["scores"][key]), r["patient_id"])
            for r in graded
            if r["scores"].get(key) is not None
        ]
        if pairs:
            values, clusters = zip(*pairs, strict=True)
            metric_rows.append(
                [label, len(values), str(bootstrap_ci(list(values), list(clusters)))]
            )
    lines += table(["Metric", "n", "Mean [95% CI]"], metric_rows)

    lines += ["", "## By category", ""]
    cat_rows = []
    for cat in CATEGORIES:
        members = [r for r in graded if r["category"] == cat]
        if not members:
            continue

        def mean(key: str, members: list[dict[str, Any]] = members) -> str:
            vals = [r["scores"][key] for r in members if r["scores"].get(key) is not None]
            return f"{sum(vals) / len(vals):.3f}" if vals else "-"

        cat_rows.append(
            [
                cat,
                len(members),
                mean("citation_recall"),
                mean("key_facts"),
                mean("faithfulness"),
            ]
        )
    lines += table(["Category", "n", "Citation recall", "Key facts", "Faithfulness"], cat_rows)

    gen_cost = [r.get("cost_usd") or 0.0 for r in rows]
    judge_cost = [((r.get("judge") or {}).get("cost_usd") or 0.0) for r in rows]
    total = [r["latency_s"]["total"] for r in rows]
    llm = [r["latency_s"]["llm"] for r in rows]
    tokens_in = [r["usage"]["input_tokens"] for r in rows]
    tokens_out = [r["usage"]["output_tokens"] for r in rows]
    lines += [
        "",
        "## Cost and latency",
        "",
        *table(
            ["", "Value"],
            [
                [
                    "Total cost (generator + judge)",
                    f"${sum(gen_cost) + sum(judge_cost):.2f}",
                ],
                ["Generator cost per case", f"${sum(gen_cost) / len(rows):.4f}"],
                ["Judge cost per case", f"${sum(judge_cost) / len(rows):.4f}"],
                ["Input tokens per case (mean)", f"{sum(tokens_in) / len(rows):.0f}"],
                ["Output tokens per case (mean)", f"{sum(tokens_out) / len(rows):.0f}"],
                [
                    "Latency p50 / p95, whole request",
                    f"{_pct(total, 50):.2f} s / {_pct(total, 95):.2f} s",
                ],
                [
                    "Latency p50 / p95, model call",
                    f"{_pct(llm, 50):.2f} s / {_pct(llm, 95):.2f} s",
                ],
            ],
        ),
    ]

    worst = sorted(
        graded,
        key=lambda r: (
            r["scores"].get("faithfulness", 1.0),
            r["scores"].get("citation_recall", 1.0),
        ),
    )[:15]
    lines += ["", "## Lowest-scoring answers", ""]
    lines += table(
        ["Question", "Faithfulness", "Citation recall", "Answer"],
        [
            [
                r["question_id"],
                r["scores"].get("faithfulness", "-"),
                f"{r['scores'].get('citation_recall', 0):.2f}",
                " ".join(s["text"] for s in r["answer"])[:160].replace("|", "/"),
            ]
            for r in worst
        ],
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n")
    return out
