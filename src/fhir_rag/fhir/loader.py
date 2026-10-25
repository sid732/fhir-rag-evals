"""Read Synthea FHIR R4 transaction bundles from the cohort directory.

The loader returns plain dicts. Typed views of single resources live in
fhir_rag.fhir.views, which keeps this module the one piece the service and
the gold-label generator share (PLAN.md D12).
"""

import gzip
import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any

type Bundle = dict[str, Any]
type Resource = dict[str, Any]

# Synthea writes these next to the patient bundles. They hold organizations
# and practitioners, not patients.
DIRECTORY_FILES = frozenset({"hospitalInformation.json.gz", "practitionerInformation.json.gz"})


def patient_bundle_paths(cohort_dir: Path) -> list[Path]:
    """Return the patient bundle files in cohort_dir, sorted by file name.

    Only `*.json.gz` files count, and DIRECTORY_FILES are skipped.
    """
    paths = (p for p in cohort_dir.glob("*.json.gz") if p.name not in DIRECTORY_FILES)
    return sorted(paths, key=lambda p: p.name)


def load_bundle(path: Path) -> Bundle:
    """Read one gzipped JSON file and return the parsed Bundle.

    Raises ValueError if the top-level resourceType isn't "Bundle".
    """
    data = json.loads(gzip.decompress(path.read_bytes()))
    if not isinstance(data, dict) or data.get("resourceType") != "Bundle":
        raise ValueError(f"{path} is not a FHIR Bundle")
    return data


def iter_resources(bundle: Bundle) -> Iterator[Resource]:
    """Yield the resource from each bundle entry, in entry order.

    A bundle without an "entry" key yields nothing; entry is optional in FHIR.
    """
    for entry in bundle.get("entry", []):
        yield entry["resource"]


def patient_of(bundle: Bundle) -> Resource:
    """Return the single Patient resource in a Synthea patient bundle."""
    for resource in iter_resources(bundle):
        if resource["resourceType"] == "Patient":
            return resource
    raise ValueError("bundle has no Patient resource")
