"""Calibrate the faithfulness judge against hand labels (design.md D14).

    python -m fhir_rag.evals.calibrate sample --run NAME [--n 50] [--set SET]
    python -m fhir_rag.evals.calibrate score [--set SET] [--run NAME]

`sample` picks judged sentences from a run and writes them to
evals/labels/SET.md for a labeler: each sentence with its whole
answer, the cards it cites, and everything the model saw. The judge's
verdicts go to SET.verdicts.jsonl so labeling stays blind. Write s, p or n on
each `label:` line (supported, partially supported, not supported), with a
trailing ? for a case you find unclear. Sentences already in another set are
skipped, so a new set is a fresh, held-out sample.

The judge flags few sentences, so a plain random sample would hold almost no
flags. Up to half the sample is sentences the judge didn't mark supported,
the rest are drawn from those it did, and each line carries the weight that
maps its stratum back to the whole run.

`score` compares the labels with the judge: agreement on the sample and on
clear cases, agreement and faithfulness weighted back to the run, Cohen's
kappa (agreement corrected for chance), and a confusion table. With --run it
scores that run's verdicts instead of the ones sampled, so a revised judge
can be scored on labels written for an earlier one (the weights still hold:
they come from how the set was drawn, not from the judge being scored). Until
agreement on clear cases reaches 90%, the judge's faithfulness numbers
shouldn't be trusted, and the report should say so.
"""

import argparse
import json
import random
import re
import sys
from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from fhir_rag.evals.common import table

LABELS_DIR = Path("evals/labels")
DEFAULT_SET = "judge_calibration"
CLASSES = ("supported", "partially_supported", "not_supported")
SHORT = {"s": "supported", "p": "partially_supported", "n": "not_supported"}

HEADER = """# Judge calibration: {run}

{n} answer sentences. Label each one by the rubric below, then run
`uv run python -m fhir_rag.evals.calibrate score --set {name}`. Don't open
`{name}.verdicts.jsonl` or the run's report until you're done.

On each `label:` line write `s` (supported), `p` (partially supported) or `n`
(not supported). Add `?` after the letter (`s?`) when the case is unclear to
you; unclear cases are reported apart from clear ones. The sentence being
labeled is in bold inside its whole answer.

The rubric, which the judge's prompt also states:

- Facts about specific entries (names, numbers, units, dates, statuses,
  reasons, how entries relate) must be stated in the cards the sentence cites.
- Claims about the whole record (most recent, latest, first or only one of its
  kind, counts, a complete list, something absent or never done) are checked
  against everything the model saw.
- `s`: every claim passes its check. `p`: the main claim passes, but a detail
  is missing from its evidence or goes beyond it. `n`: the main claim fails or
  the evidence contradicts it; a fact about an entry fails when the sentence
  cites nothing.
"""

_HEADING = re.compile(r"^## \d+\. `([^`]+)`$", re.M)
_LABEL = re.compile(r"^label:[ \t]*([spn])?(\?)?[ \t]*$", re.M | re.I)


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


def stratified(
    items: Sequence[tuple[str, str]], n: int, seed: int = 0
) -> list[tuple[str, str, float]]:
    """(key, verdict) pairs -> (key, verdict, weight). Flags fill up to half of n."""
    rng = random.Random(seed)
    flagged = [x for x in items if x[1] != "supported"]
    passed = [x for x in items if x[1] == "supported"]
    rng.shuffle(flagged)
    rng.shuffle(passed)
    picked_flagged = flagged[: n // 2]
    picked_passed = passed[: n - len(picked_flagged)]
    picked = [
        (key, verdict, len(pool) / len(chosen))
        for pool, chosen in ((flagged, picked_flagged), (passed, picked_passed))
        for key, verdict in chosen
    ]
    rng.shuffle(picked)
    return picked


def _item(number: int, key: str, row: dict[str, Any], i: int, context: list[Any]) -> str:
    from fhir_rag.evals.judge import cited_excerpts

    sentence = row["answer"][i]
    answer = " ".join(
        f"**{s['text']}**" if j == i else s["text"] for j, s in enumerate(row["answer"])
    )
    cited = [
        f"- `[{c}]` {text}" for c in sentence["citations"] for text in cited_excerpts(c, context)
    ]
    seen = "\n".join(f"[{r.chunk.chunk_id}] {r.chunk.text}" for r in context)
    return "\n".join(
        [
            f"## {number}. `{key}`",
            "",
            f"Question: {row['question']}",
            "",
            f"Answer: {answer}",
            "",
            "Cards this sentence cites:",
            "",
            *(cited or ["- (cites nothing)"]),
            "",
            f"<details><summary>Everything the model saw ({len(context)} cards)</summary>",
            "",
            "```text",
            seen,
            "```",
            "",
            "</details>",
            "",
            "label: ",
            "",
        ]
    )


def set_paths(name: str) -> tuple[Path, Path]:
    """The label sheet and the judge-verdicts file of one calibration set."""
    return LABELS_DIR / f"{name}.md", LABELS_DIR / f"{name}.verdicts.jsonl"


def _judged(run: str) -> dict[str, tuple[dict[str, Any], int, str]]:
    """Every judged sentence of a run by key: (row, sentence index, verdict)."""
    rows = [json.loads(line) for line in (Path("evals/runs") / run / "results.jsonl").open()]
    by_key = {}
    for r in rows:
        for i, verdict in enumerate((r.get("judge") or {}).get("verdicts", [])):
            by_key[f"{r['question_id']}#{r['rep']}#{i}"] = (r, i, verdict)
    return by_key


def sample(run: str, n: int, name: str, seed: int = 0) -> int:
    from fhir_rag.config import get_settings
    from fhir_rag.evals.rejudge import load_chunks, rebuild_context
    from fhir_rag.store import Store

    sheet, verdicts_path = set_paths(name)
    if sheet.exists() and read_labels(sheet.read_text()):
        print(f"{sheet} already has labels; pick another --set", file=sys.stderr)
        return 2
    taken = {
        json.loads(line)["key"]
        for other in LABELS_DIR.glob("*.verdicts.jsonl")
        if other != verdicts_path
        for line in other.open()
        if line.strip()
    }
    by_key = _judged(run)
    picked = stratified([(k, v) for k, (_, _, v) in by_key.items() if k not in taken], n, seed)
    store = Store(get_settings().db_path)
    try:
        chunks = load_chunks(store, [by_key[k][0] for k, _, _ in picked])
    finally:
        store.close()
    parts = [HEADER.format(run=run, n=len(picked), name=name)]
    for number, (key, _, _) in enumerate(picked, start=1):
        row, i, _ = by_key[key]
        context = rebuild_context(row, chunks[row["patient_id"]])
        parts.append(_item(number, key, row, i, context))
    LABELS_DIR.mkdir(parents=True, exist_ok=True)
    sheet.write_text("\n".join(parts))
    with verdicts_path.open("w") as f:
        for key, verdict, weight in picked:
            f.write(json.dumps({"key": key, "judge": verdict, "weight": weight}) + "\n")
    skipped = f" ({len(taken)} already in other sets skipped)" if taken else ""
    print(f"wrote {len(picked)} sentences to {sheet}{skipped}; label each one, then `score`")
    return 0


@dataclass(frozen=True)
class Label:
    label: str
    clear: bool


def read_labels(text: str) -> dict[str, Label]:
    """Labels filled in on the sheet, by key. Blank label lines are skipped."""
    headings = list(_HEADING.finditer(text))
    labels = {}
    for heading, following in zip(headings, [*headings[1:], None], strict=True):
        section = text[heading.end() : following.start() if following else len(text)]
        section = section[section.rfind("</details>") :]  # card text can't fake a label
        match = _LABEL.search(section)
        if match and match.group(1):
            labels[heading.group(1)] = Label(SHORT[match.group(1).lower()], not match.group(2))
    return labels


def summarize(labels: dict[str, Label], verdicts: dict[str, dict[str, Any]]) -> list[str]:
    keys = sorted(k for k in labels if k in verdicts)
    human = [labels[k].label for k in keys]
    judge = [verdicts[k]["judge"] for k in keys]
    weight = [float(verdicts[k].get("weight", 1.0)) for k in keys]
    agree = [h == j for h, j in zip(human, judge, strict=True)]
    clear = [a for a, k in zip(agree, keys, strict=True) if labels[k].clear]

    def weighted(values: Sequence[bool]) -> float:
        return sum(w for w, v in zip(weight, values, strict=True) if v) / sum(weight)

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
    return [
        f"{len(keys)} of {len(verdicts)} sentences labeled, "
        f"{len(keys) - len(clear)} marked unclear",
        f"agreement {sum(agree) / len(keys):.3f} on the sample, "
        f"{sum(clear) / len(clear) if clear else 0:.3f} on clear cases",
        f"weighted back to the run: agreement {weighted(agree):.3f}; sentences supported "
        f"{weighted([h == 'supported' for h in human]):.3f} by the labels, "
        f"{weighted([j == 'supported' for j in judge]):.3f} by the judge "
        "(per sentence, not the report's per-answer mean)",
        f"Cohen's kappa {cohen_kappa(human, judge):.3f}; "
        f"supported vs not {cohen_kappa(_binary(human), _binary(judge)):.3f} (on the sample)",
        *table(["labels \\ judge", *CLASSES], rows),
    ]


def score(name: str, run: str | None = None) -> int:
    sheet, verdicts_path = set_paths(name)
    labels = read_labels(sheet.read_text())
    verdicts = {row["key"]: row for row in map(json.loads, verdicts_path.open())}
    if run is not None:
        judged = _judged(run)
        missing = [k for k in verdicts if k not in judged]
        if missing:
            print(f"{run} has no verdict for {len(missing)} sentences of {name}", file=sys.stderr)
            return 2
        verdicts = {k: v | {"judge": judged[k][2]} for k, v in verdicts.items()}
    if not any(k in verdicts for k in labels):
        print("no labeled sentences yet", file=sys.stderr)
        return 1
    print("\n".join(summarize(labels, verdicts)))
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    s = sub.add_parser("sample")
    s.add_argument("--run", required=True)
    s.add_argument("--n", type=int, default=50)
    s.add_argument("--set", dest="name", default=DEFAULT_SET)
    c = sub.add_parser("score")
    c.add_argument("--set", dest="name", default=DEFAULT_SET)
    c.add_argument("--run", default=None, help="score this run's verdicts instead")
    args = parser.parse_args(argv)
    if args.command == "sample":
        return sample(args.run, args.n, args.name)
    return score(args.name, args.run)


if __name__ == "__main__":
    sys.exit(main())
