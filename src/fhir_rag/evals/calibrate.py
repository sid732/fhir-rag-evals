"""Calibrate the faithfulness judge against hand labels (PLAN.md D14).

    python -m fhir_rag.evals.calibrate sample --run NAME [--n 50]
    python -m fhir_rag.evals.calibrate score

`sample` picks judged sentences from a run and writes them to
evals/labels/judge_calibration.jsonl for a human to label, with the judge's
verdicts kept in a separate file so labeling stays blind. Fill in "label"
on every line with supported, partially_supported or not_supported.

`score` compares the labels with the judge: raw agreement, Cohen's kappa
(agreement corrected for chance), and a confusion table. Until agreement on
clear cases reaches 90%, the judge's faithfulness numbers shouldn't be
trusted, and the report should say so.
"""

import argparse
import json
import random
import sys
from collections import Counter
from collections.abc import Sequence
from pathlib import Path

from fhir_rag.evals.common import table

LABELS = Path("evals/labels/judge_calibration.jsonl")
VERDICTS = Path("evals/labels/judge_verdicts.jsonl")
CLASSES = ("supported", "partially_supported", "not_supported")


def cohen_kappa(a: Sequence[str], b: Sequence[str]) -> float:
    """Agreement between two raters, corrected for agreement expected by chance."""
    n = len(a)
    if n == 0:
        return 0.0
    observed = sum(x == y for x, y in zip(a, b, strict=True)) / n
    ca, cb = Counter(a), Counter(b)
    expected = sum(ca[c] * cb[c] for c in set(a) | set(b)) / (n * n)
    return 1.0 if expected == 1 else (observed - expected) / (1 - expected)


def _binary(labels: Sequence[str]) -> list[str]:
    """Collapse to supported vs not, the distinction faithfulness reports."""
    return ["supported" if x == "supported" else "not" for x in labels]


def sample(run: str, n: int, seed: int = 0) -> int:
    rows = [json.loads(line) for line in (Path("evals/runs") / run / "results.jsonl").open()]
    items = []
    for r in rows:
        judge = r.get("judge")
        if not judge:
            continue
        for i, sentence in enumerate(r["answer"]):
            if sentence["citations"]:
                items.append((r, i, sentence, judge["verdicts"][i]))
    random.Random(seed).shuffle(items)
    items = items[:n]
    from fhir_rag.config import get_settings
    from fhir_rag.store import Store

    store = Store(get_settings().db_path)
    LABELS.parent.mkdir(parents=True, exist_ok=True)
    with LABELS.open("w") as labels, VERDICTS.open("w") as verdicts:
        for r, i, sentence, verdict in items:
            key = f"{r['question_id']}#{r['rep']}#{i}"
            cards = []
            for c in sentence["citations"]:
                chunk = next(
                    (
                        ch
                        for ch in store.chunks(r["patient_id"])
                        if c in (ch.chunk_id, ch.resource_ref)
                    ),
                    None,
                )
                cards.append(chunk.text if chunk else f"(missing card {c})")
            labels.write(
                json.dumps(
                    {
                        "key": key,
                        "question": r["question"],
                        "sentence": sentence["text"],
                        "cited_cards": cards,
                        "label": None,
                    }
                )
                + "\n"
            )
            verdicts.write(json.dumps({"key": key, "judge": verdict}) + "\n")
    print(f"wrote {len(items)} sentences to {LABELS}; label each one, then run `score`")
    return 0


def score() -> int:
    labels = {
        row["key"]: row["label"]
        for row in map(json.loads, LABELS.open())
        if row.get("label") in CLASSES
    }
    verdicts = {row["key"]: row["judge"] for row in map(json.loads, VERDICTS.open())}
    keys = sorted(k for k in labels if k in verdicts)
    if not keys:
        print("no labeled sentences yet", file=sys.stderr)
        return 1
    human = [labels[k] for k in keys]
    judge = [verdicts[k] for k in keys]
    agreement = sum(h == j for h, j in zip(human, judge, strict=True)) / len(keys)
    rows = [
        [
            h,
            *(
                sum(1 for a, b in zip(human, judge, strict=True) if a == h and b == j)
                for j in CLASSES
            ),
        ]
        for h in CLASSES
    ]
    print(f"{len(keys)} labeled sentences")
    print(f"agreement {agreement:.3f}, Cohen's kappa {cohen_kappa(human, judge):.3f}")
    print(f"supported vs not: kappa {cohen_kappa(_binary(human), _binary(judge)):.3f}")
    print("\n".join(table(["human \\ judge", *CLASSES], rows)))
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    s = sub.add_parser("sample")
    s.add_argument("--run", required=True)
    s.add_argument("--n", type=int, default=50)
    sub.add_parser("score")
    args = parser.parse_args(argv)
    return sample(args.run, args.n) if args.command == "sample" else score()


if __name__ == "__main__":
    sys.exit(main())
