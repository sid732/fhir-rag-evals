import gzip
import json
from pathlib import Path
from typing import Any

import pytest

from fhir_rag.fhir.loader import (
    DIRECTORY_FILES,
    iter_resources,
    load_bundle,
    patient_bundle_paths,
)

COHORT_DIR = Path(__file__).resolve().parents[1] / "data" / "cohort"


def _bundle(*resources: dict[str, Any]) -> dict[str, Any]:
    entries = [{"fullUrl": f"urn:uuid:{r['id']}", "resource": r} for r in resources]
    return {"resourceType": "Bundle", "type": "transaction", "entry": entries}


def _write_gz(path: Path, obj: dict[str, Any]) -> Path:
    path.write_bytes(gzip.compress(json.dumps(obj).encode()))
    return path


def test_patient_bundle_paths_sorted_and_skips_other_files(tmp_path: Path) -> None:
    names = ["b.json.gz", "a.json.gz", *DIRECTORY_FILES, "MANIFEST.sha256", "x.json"]
    for name in names:
        (tmp_path / name).write_bytes(b"")
    assert [p.name for p in patient_bundle_paths(tmp_path)] == [
        "a.json.gz",
        "b.json.gz",
    ]


def test_load_bundle_round_trips(tmp_path: Path) -> None:
    bundle = _bundle({"resourceType": "Patient", "id": "p1"})
    assert load_bundle(_write_gz(tmp_path / "p1.json.gz", bundle)) == bundle


def test_load_bundle_rejects_a_non_bundle(tmp_path: Path) -> None:
    path = _write_gz(tmp_path / "p1.json.gz", {"resourceType": "Patient", "id": "p1"})
    with pytest.raises(ValueError, match="Bundle"):
        load_bundle(path)


def test_iter_resources_keeps_entry_order() -> None:
    bundle = _bundle(
        {"resourceType": "Patient", "id": "p1"},
        {"resourceType": "Encounter", "id": "e1"},
    )
    assert [r["id"] for r in iter_resources(bundle)] == ["p1", "e1"]


def test_iter_resources_on_bundle_without_entries() -> None:
    assert list(iter_resources({"resourceType": "Bundle", "type": "transaction"})) == []


def test_committed_cohort_matches_its_manifest() -> None:
    # generate.sh writes the manifest. A missing or extra bundle means the
    # cohort and the gold labels can drift apart.
    lines = (COHORT_DIR / "MANIFEST.sha256").read_text().splitlines()
    listed = {line.split()[1] + ".gz" for line in lines}
    on_disk = {p.name for p in patient_bundle_paths(COHORT_DIR)}
    assert len(on_disk) == 15
    assert on_disk | DIRECTORY_FILES == listed
