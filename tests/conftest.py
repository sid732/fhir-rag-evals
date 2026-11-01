"""Fixtures: the tiny cohort from tests/cohort.py, indexed with HashEmbedder."""

import gzip
import json
from collections.abc import Iterator
from pathlib import Path

import pytest
from cohort import AS_OF, bundle, patient_one, patient_two

from fhir_rag.config import Settings
from fhir_rag.ingest import build_index
from fhir_rag.retrieval.dense import HashEmbedder
from fhir_rag.retrieval.retriever import Retriever
from fhir_rag.store import Store


@pytest.fixture
def cohort_dir(tmp_path: Path) -> Path:
    cohort = tmp_path / "cohort"
    cohort.mkdir()
    for name, resources in [("p1", patient_one()), ("p2", patient_two())]:
        (cohort / f"{name}.json.gz").write_bytes(
            gzip.compress(json.dumps(bundle(resources)).encode())
        )
    return cohort


@pytest.fixture
def store(tmp_path: Path, cohort_dir: Path) -> Iterator[Store]:
    s = Store(tmp_path / "index.sqlite")
    build_index(cohort_dir, s, HashEmbedder(), AS_OF)
    yield s
    s.close()


@pytest.fixture
def retriever(store: Store) -> Retriever:
    return Retriever(store, HashEmbedder())


@pytest.fixture
def settings(tmp_path: Path, cohort_dir: Path) -> Settings:
    return Settings(
        _env_file=None,  # don't read a developer's .env
        llm_backend="api",  # nor run a real `claude` if the shell picks the CLI backend
        cohort_dir=cohort_dir,
        db_path=tmp_path / "index.sqlite",
        record_as_of=AS_OF,
        embedding_model=HashEmbedder.model_name,
    )
