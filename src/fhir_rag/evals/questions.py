"""The labeled question set (design.md D12) and its dev/test split.

Gold evidence is a list of groups. Each group is a set of interchangeable
resource refs: citing or retrieving any one of them counts for the group.
"Latest HbA1c" has one group with one ref; "what was prescribed for
diabetes?" has one group per drug, holding every prescription of that drug
for that reason. An empty list means the record can't answer the question.
"""

import hashlib
import json
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict

type Category = Literal[
    "fact_lookup", "values_dates", "lay_terms", "multi_step", "rare_history", "not_in_record"
]
type Source = Literal["template", "drafted", "human"]
type Split = Literal["dev", "test"]

CATEGORIES: tuple[Category, ...] = (
    "fact_lookup",
    "values_dates",
    "lay_terms",
    "multi_step",
    "rare_history",
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


def assign_splits(
    questions: Iterable[Question], fixed: Mapping[str, Split] | None = None
) -> list[Question]:
    """Dev or test for every question, decided once and then never moved.

    A question in `fixed` (the split file as last built) keeps its split. A
    new one goes to dev when the hash of its id falls in the first 60% of the
    hash range, so its split depends on nothing but its id. The first build
    ranked hashes within each category instead, an exact 60/40 that moved
    other questions' splits whenever one was added; `fixed` keeps the splits
    it made.
    """
    fixed = fixed or {}
    out = [q.model_copy(update={"split": fixed.get(q.id) or _split_of(q.id)}) for q in questions]
    return sorted(out, key=lambda q: q.id)


def _split_of(question_id: str) -> Split:
    share = int(hashlib.sha256(question_id.encode()).hexdigest()[:8], 16) / 16**8
    return "dev" if share < DEV_SHARE else "test"


def load_questions(path: Path, split: Split | None = None) -> list[Question]:
    questions = [
        Question.model_validate_json(line) for line in path.read_text().splitlines() if line.strip()
    ]
    return [q for q in questions if split is None or q.split == split]


def save_questions(path: Path, questions: Iterable[Question]) -> None:
    lines = [json.dumps(q.model_dump(mode="json"), sort_keys=True) for q in questions]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")
