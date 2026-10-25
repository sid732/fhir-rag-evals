"""Dense retrieval: local embeddings and exact cosine search (PLAN.md D7, D8)."""

import hashlib
import re
from collections.abc import Sequence
from typing import Protocol

import numpy as np

from fhir_rag.store import Matrix


class Embedder(Protocol):
    model_name: str

    def embed_documents(self, texts: Sequence[str]) -> Matrix: ...

    def embed_query(self, text: str) -> Matrix: ...


def _normalize(matrix: Matrix) -> Matrix:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    return (matrix / np.maximum(norms, 1e-12)).astype(np.float32)


class FastEmbedEmbedder:
    """bge-small-en-v1.5 (or another fastembed model) on ONNX Runtime, CPU only.

    BGE models expect a query instruction prefix; fastembed's query_embed
    adds the model's own query handling, and passage_embed is used for cards.
    """

    def __init__(self, model_name: str, batch_size: int = 256) -> None:
        from fastembed import TextEmbedding  # imported here: loading takes seconds

        self.model_name = model_name
        self._batch_size = batch_size
        self._model = TextEmbedding(model_name)

    def embed_documents(self, texts: Sequence[str]) -> Matrix:
        vectors = list(self._model.passage_embed(list(texts), batch_size=self._batch_size))
        return _normalize(np.asarray(vectors, dtype=np.float32))

    def embed_query(self, text: str) -> Matrix:
        vector = next(iter(self._model.query_embed(text)))
        row: Matrix = _normalize(np.asarray([vector], dtype=np.float32))[0]
        return row


class HashEmbedder:
    """Deterministic bag-of-words vectors for tests; no model download."""

    model_name = "hash-test"

    def __init__(self, dim: int = 256) -> None:
        self._dim = dim

    def _vector(self, text: str) -> Matrix:
        vec = np.zeros(self._dim, dtype=np.float32)
        for token in re.findall(r"[a-z0-9]+", text.lower()):
            bucket = int(hashlib.md5(token.encode()).hexdigest(), 16) % self._dim
            vec[bucket] += 1.0
        return vec

    def embed_documents(self, texts: Sequence[str]) -> Matrix:
        if not texts:
            return np.zeros((0, self._dim), dtype=np.float32)
        return _normalize(np.stack([self._vector(t) for t in texts]))

    def embed_query(self, text: str) -> Matrix:
        row: Matrix = _normalize(self._vector(text)[None, :])[0]
        return row


class DenseIndex:
    """Exact cosine similarity over one patient's card vectors."""

    def __init__(self, chunk_ids: list[str], matrix: Matrix) -> None:
        self.chunk_ids = chunk_ids
        self._matrix = matrix

    def scores(self, query_vector: Matrix) -> Matrix:
        if not self.chunk_ids:
            return np.zeros(0, dtype=np.float32)
        result: Matrix = self._matrix @ query_vector
        return result
