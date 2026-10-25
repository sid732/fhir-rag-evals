"""The labeled question set (PLAN.md D12) and its dev/test split.

Gold evidence is a list of groups. Each group is a set of interchangeable
resource refs: citing or retrieving any one of them counts for the group.
"Latest HbA1c" has one group with one ref; "what was prescribed for
diabetes?" has one group per drug, holding every prescription of that drug
for that reason. An empty list means the record can't answer the question.
"""

import hashlib
import json
from collections.abc import Iterable
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict

type Category = Literal["fact_lookup", "values_dates", "lay_terms", "multi_step", "not_in_record"]
type Source = Literal["template", "drafted", "human"]
type Split = Literal["dev", "test"]

CATEGORIES: tuple[Category, ...] = (
    "fact_lookup",
    "values_dates",
    "lay_terms",
    "multi_step",
    "not_in_record",
)
DEV_SHARE = 0.6


class Question(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str
    patient_id: str
    question: str
    category: Category
    gold_groups: list[list[str]]
    key_facts: list[str] = []  # strings a correct answer must contain
    source: Source
    split: Split | None = None
    note: str = ""

    @property
    def answerable(self) -> bool:
        return bool(self.gold_groups)


def assign_splits(questions: Iterable[Question]) -> list[Question]:
    """60/40 dev/test within each category, decided by a hash of the id.

    Hash order is fixed before any tuning, doesn't depend on file order, and
    keeps a question's split stable when other questions are added.
    """
    by_category: dict[str, list[Question]] = {}
    for q in questions:
        by_category.setdefault(q.category, []).append(q)
    out: list[Question] = []
    for category in CATEGORIES:
        group = sorted(
            by_category.get(category, []),
            key=lambda q: hashlib.sha256(q.id.encode()).hexdigest(),
        )
        n_dev = round(len(group) * DEV_SHARE)
        out += [
            q.model_copy(update={"split": "dev" if i < n_dev else "test"})
            for i, q in enumerate(group)
        ]
    return sorted(out, key=lambda q: q.id)


def load_questions(path: Path, split: Split | None = None) -> list[Question]:
    questions = [
        Question.model_validate_json(line) for line in path.read_text().splitlines() if line.strip()
    ]
    return [q for q in questions if split is None or q.split == split]


def save_questions(path: Path, questions: Iterable[Question]) -> None:
    lines = [json.dumps(q.model_dump(mode="json"), sort_keys=True) for q in questions]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")
