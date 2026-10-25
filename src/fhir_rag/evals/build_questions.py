"""Build evals/questions/questions.jsonl from the templates and drafted questions.

    python -m fhir_rag.evals.build_questions

Template questions come from fhir_rag.evals.templates. Drafted questions live
in evals/questions/drafted.jsonl (written by hand, with gold refs checked
against the record). The split is assigned here, once, by hash of the id.
"""

import sys
from collections import Counter
from collections.abc import Sequence
from pathlib import Path

from fhir_rag.config import get_settings
from fhir_rag.evals.questions import (
    Question,
    assign_splits,
    load_questions,
    save_questions,
)
from fhir_rag.evals.templates import template_questions
from fhir_rag.fhir.loader import (
    iter_resources,
    load_bundle,
    patient_bundle_paths,
    patient_of,
)

QUESTIONS_DIR = Path("evals/questions")
DRAFTED = QUESTIONS_DIR / "drafted.jsonl"
OUTPUT = QUESTIONS_DIR / "questions.jsonl"


def check_gold(questions: Sequence[Question], refs_by_patient: dict[str, set[str]]) -> list[str]:
    """Problems with gold labels: unknown patients or refs from another record."""
    problems = []
    seen: set[str] = set()
    for q in questions:
        if q.id in seen:
            problems.append(f"{q.id}: duplicate id")
        seen.add(q.id)
        refs = refs_by_patient.get(q.patient_id)
        if refs is None:
            problems.append(f"{q.id}: unknown patient {q.patient_id}")
            continue
        for ref in (r for group in q.gold_groups for r in group):
            if ref not in refs:
                problems.append(f"{q.id}: {ref} is not in patient {q.patient_id[:8]}'s record")
        if (q.category == "not_in_record") == q.answerable:
            problems.append(f"{q.id}: category and gold disagree about answerability")
    return problems


def main(argv: Sequence[str] | None = None) -> int:
    settings = get_settings()
    questions: list[Question] = []
    refs_by_patient: dict[str, set[str]] = {}
    for path in patient_bundle_paths(settings.cohort_dir):
        bundle = load_bundle(path)
        pid = patient_of(bundle)["id"]
        refs_by_patient[pid] = {f"{r['resourceType']}/{r['id']}" for r in iter_resources(bundle)}
        questions += template_questions(pid, bundle)
    if DRAFTED.exists():
        questions += load_questions(DRAFTED)

    problems = check_gold(questions, refs_by_patient)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    final = assign_splits(questions)
    save_questions(OUTPUT, final)
    counts = Counter((q.category, q.split) for q in final)
    print(f"{len(final)} questions -> {OUTPUT}")
    for category in sorted({c for c, _ in counts}):
        dev, test = counts[(category, "dev")], counts[(category, "test")]
        print(f"  {category:14} dev {dev:3}  test {test:3}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
