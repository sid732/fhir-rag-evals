"""Okapi BM25 over one patient's cards (PLAN.md D6).

Written out rather than taken from a library: a patient has at most ~14k
cards, so scoring every posting with numpy is fast, and every term of the
formula is visible:

    score(d, q) = sum over t in q of
        idf(t) * tf(t, d) * (k1 + 1) / (tf(t, d) + k1 * (1 - b + b * len(d) / avglen))
    idf(t) = ln(1 + (N - df(t) + 0.5) / (df(t) + 0.5))

k1 sets how fast repeated terms saturate; b sets how much long cards are
penalized. The defaults are the common Lucene values.
"""

import math
import re
from collections import Counter, defaultdict

import numpy as np

from fhir_rag.store import Matrix

_TOKEN = re.compile(r"[a-z0-9]+(?:\.[0-9]+)?")
STOPWORDS = frozenset(
    """
    a an and any are as at be been by did do does for from had has have he her his
    how i in is it its me my of on or our patient patient's patients she so that the
    their them there they this to was were what when which who why with you your
    """.split()  # noqa: SIM905 (one word list is easier to read than 60 quoted strings)
)


def tokenize(text: str) -> list[str]:
    """Lowercase alphanumeric tokens, decimals kept whole, stopwords removed."""
    return [t for t in _TOKEN.findall(text.lower()) if t not in STOPWORDS]


class BM25Index:
    def __init__(self, chunk_ids: list[str], texts: list[str], k1: float = 1.5, b: float = 0.75):
        self.chunk_ids = chunk_ids
        self._k1 = k1
        docs = [Counter(tokenize(t)) for t in texts]
        lengths = np.array([sum(d.values()) for d in docs], dtype=np.float32)
        avg = float(lengths.mean()) if len(docs) else 1.0
        # Per-document length normalization, precomputed once.
        self._norm = k1 * (1 - b + b * lengths / max(avg, 1e-9))
        postings: dict[str, tuple[list[int], list[int]]] = defaultdict(lambda: ([], []))
        for i, doc in enumerate(docs):
            for term, tf in doc.items():
                postings[term][0].append(i)
                postings[term][1].append(tf)
        n = len(docs)
        self._postings = {
            term: (
                np.array(idx),
                np.array(tf, dtype=np.float32),
                self._idf(n, len(idx)),
            )
            for term, (idx, tf) in postings.items()
        }

    @staticmethod
    def _idf(n: int, df: int) -> float:
        return math.log(1 + (n - df + 0.5) / (df + 0.5))

    def scores(self, query: str) -> Matrix:
        scores = np.zeros(len(self.chunk_ids), dtype=np.float32)
        for term in set(tokenize(query)):
            if term not in self._postings:
                continue
            idx, tf, idf = self._postings[term]
            scores[idx] += idf * tf * (self._k1 + 1) / (tf + self._norm[idx])
        return scores
