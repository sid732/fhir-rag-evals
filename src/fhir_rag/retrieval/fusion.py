"""Reciprocal Rank Fusion (PLAN.md D6).

Each list contributes 1 / (k + rank) for every item it ranks, ranks starting
at 1. Only ranks matter, so BM25 scores and cosine similarities never need to
share a scale. k = 60 is the value from the original RRF paper; it keeps one
first-place finish from outweighing steady agreement across lists.
"""

from collections import defaultdict
from collections.abc import Sequence


def rrf(rankings: Sequence[Sequence[str]], k: int = 60) -> list[tuple[str, float]]:
    """Fused (id, score) pairs, best first; ties broken by id for stable output."""
    scores: dict[str, float] = defaultdict(float)
    for ranking in rankings:
        for rank, item in enumerate(ranking, start=1):
            scores[item] += 1.0 / (k + rank)
    return sorted(scores.items(), key=lambda pair: (-pair[1], pair[0]))
