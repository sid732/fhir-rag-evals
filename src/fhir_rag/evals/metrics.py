"""Metric definitions (PLAN.md D13). Pure functions over refs and text.

Gold evidence is a list of groups of interchangeable refs (questions.py).
Retrieved and cited items may be card ids ("DocumentReference/x#2"); they
are compared at the resource level.
"""

import random
import re
from collections.abc import Sequence
from dataclasses import dataclass


def resource_of(item: str) -> str:
    """'DocumentReference/x#2' -> 'DocumentReference/x'."""
    return item.split("#", 1)[0]


def _ranked_resources(ranked: Sequence[str], k: int) -> list[str]:
    """Top-k items as resources, duplicates (several note chunks) collapsed."""
    out: list[str] = []
    for item in ranked[:k]:
        ref = resource_of(item)
        if ref not in out:
            out.append(ref)
    return out


def hit_at_k(ranked: Sequence[str], gold: Sequence[Sequence[str]], k: int) -> float:
    """1 if any gold group has a member in the top k, else 0."""
    top = set(_ranked_resources(ranked, k))
    return float(any(top & set(g) for g in gold))


def recall_at_k(ranked: Sequence[str], gold: Sequence[Sequence[str]], k: int) -> float:
    """Share of gold groups with a member in the top k."""
    if not gold:
        return 0.0
    top = set(_ranked_resources(ranked, k))
    return sum(1 for g in gold if top & set(g)) / len(gold)


def mrr_at_k(ranked: Sequence[str], gold: Sequence[Sequence[str]], k: int) -> float:
    """1 / rank of the first item in any gold group, 0 if none in the top k."""
    members = {ref for g in gold for ref in g}
    for rank, item in enumerate(ranked[:k], start=1):
        if resource_of(item) in members:
            return 1.0 / rank
    return 0.0


@dataclass(frozen=True)
class CitationScores:
    validity: float | None  # raw citations that name a card in the context; None if none
    precision: float  # valid cited resources that belong to some gold group
    recall: float  # gold groups with at least one valid cited member


def citation_scores(
    raw: Sequence[str], retrieved: Sequence[str], gold: Sequence[Sequence[str]]
) -> CitationScores:
    """Scores for one answer.

    Validity looks at every citation the model wrote. Precision and recall
    look only at the valid ones, since invalid citations are removed before
    the answer is shown.
    """
    context = set(retrieved) | {resource_of(r) for r in retrieved}
    valid = [c for c in raw if c in context]
    validity = len(valid) / len(raw) if raw else None
    cited_refs = {resource_of(c) for c in valid}
    if not cited_refs:
        return CitationScores(validity, 0.0, 0.0)
    members = {ref for g in gold for ref in g}
    precision = len(cited_refs & members) / len(cited_refs)
    recall = sum(1 for g in gold if cited_refs & set(g)) / len(gold) if gold else 0.0
    return CitationScores(validity, precision, recall)


_NUMBER = re.compile(r"(?<![\w.])-?\d+(?:\.\d+)?(?![\w])")
_DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")


def numbers_in(text: str) -> set[float]:
    """Numbers in text as floats, with dates removed first."""
    return {float(n) for n in _NUMBER.findall(_DATE.sub(" ", text))}


def dates_in(text: str) -> set[str]:
    return set(_DATE.findall(text))


def unsupported_numbers_and_dates(sentence: str, evidence: Sequence[str]) -> list[str]:
    """Numbers and dates in the sentence that appear in none of its cited cards.

    The deterministic half of faithfulness (D13): a wrong lab value or date
    is the most harmful error, and this check is free and exact.
    """
    joined = " ".join(evidence)
    known_numbers = numbers_in(joined)
    known_dates = dates_in(joined)
    missing = [d for d in sorted(dates_in(sentence)) if d not in known_dates]
    missing += [f"{n:g}" for n in sorted(numbers_in(sentence)) if n not in known_numbers]
    return missing


def key_facts_present(answer: str, key_facts: Sequence[str]) -> float:
    """Share of expected facts found in the answer. Numbers compare as numbers."""
    if not key_facts:
        return 1.0
    answer_numbers = numbers_in(answer)
    answer_dates = dates_in(answer)
    found = 0
    for fact in key_facts:
        if _DATE.fullmatch(fact):
            found += fact in answer_dates
        else:
            try:
                found += float(fact) in answer_numbers
            except ValueError:
                found += fact.lower() in answer.lower()
    return found / len(key_facts)


@dataclass(frozen=True)
class Abstention:
    """Counts for answerable vs not-in-record questions (PLAN.md D11)."""

    answered_answerable: int = 0
    abstained_answerable: int = 0  # false abstention
    answered_unanswerable: int = 0  # the worst cell: an answer the record can't support
    abstained_unanswerable: int = 0

    def add(self, answerable: bool, abstained: bool) -> "Abstention":
        fields = {
            (True, False): "answered_answerable",
            (True, True): "abstained_answerable",
            (False, False): "answered_unanswerable",
            (False, True): "abstained_unanswerable",
        }
        name = fields[(answerable, abstained)]
        return Abstention(**{**self.__dict__, name: getattr(self, name) + 1})

    @property
    def abstain_precision(self) -> float:
        total = self.abstained_answerable + self.abstained_unanswerable
        return self.abstained_unanswerable / total if total else 0.0

    @property
    def abstain_recall(self) -> float:
        total = self.answered_unanswerable + self.abstained_unanswerable
        return self.abstained_unanswerable / total if total else 0.0


@dataclass(frozen=True)
class Interval:
    mean: float
    low: float
    high: float
    n: int

    def __str__(self) -> str:
        return f"{self.mean:.3f} [{self.low:.3f}, {self.high:.3f}]"


def bootstrap_ci(
    values: Sequence[float],
    clusters: Sequence[str],
    reps: int = 2000,
    seed: int = 0,
    level: float = 0.95,
) -> Interval:
    """Mean with a cluster-bootstrap confidence interval.

    Resamples patients (clusters), not single questions, because questions
    about the same patient are correlated; the interval is wider and more
    honest than a per-question bootstrap.
    """
    if not values:
        return Interval(0.0, 0.0, 0.0, 0)
    by_cluster: dict[str, list[float]] = {}
    for value, cluster in zip(values, clusters, strict=True):
        by_cluster.setdefault(cluster, []).append(value)
    groups = list(by_cluster.values())
    rng = random.Random(seed)
    means = []
    for _ in range(reps):
        sample = [v for _ in groups for v in rng.choice(groups)]
        means.append(sum(sample) / len(sample))
    means.sort()
    tail = (1 - level) / 2
    low = means[int(tail * reps)]
    high = means[min(reps - 1, int((1 - tail) * reps))]
    return Interval(sum(values) / len(values), low, high, len(values))
