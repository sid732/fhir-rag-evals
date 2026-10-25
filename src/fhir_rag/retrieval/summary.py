"""The pinned patient summary: cards every answer gets, whatever the question.

The first retrieval eval (evals/reports/retrieval-dev.md history) showed two
kinds of question that similarity search can't serve, because the deciding
property isn't in the words:

- "current" lists: active problems, active medications, allergies. A resolved
  sinusitis card looks just like an active one to BM25 and to embeddings.
- recency: "most recent visit", "vaccines in the last year".

An EHR answers these with the summary panel shown on every chart: problem
list, medication list, allergies, recent visits. This module picks the same
cards with structured filters at ingest time, and the retriever puts them in
front of the ranked results.
"""

from collections.abc import Iterable

from fhir_rag.fhir.loader import Resource
from fhir_rag.fhir.views import (
    AllergyIntoleranceView,
    ConditionView,
    EncounterView,
    ImmunizationView,
    MedicationRequestView,
    day,
    parse_view,
)

RECENT_VISITS = 3
IMMUNIZATION_MONTHS = 12


def _months_before(as_of: str, months: int) -> str:
    year, month = int(as_of[:4]), int(as_of[5:7])
    total = year * 12 + (month - 1) - months
    return f"{total // 12:04d}-{total % 12 + 1:02d}{as_of[7:]}"


def pinned_refs(resources: Iterable[Resource], as_of: str) -> list[str]:
    """Refs of the summary cards for one patient, in display order."""
    problems, medications, allergies, visits, shots = [], [], [], [], []
    since = _months_before(as_of, IMMUNIZATION_MONTHS)
    for resource in resources:
        match parse_view(resource):
            case ConditionView() as v if v.status == "active":
                problems.append((day(v.onset_date_time) or "", v.ref))
            case MedicationRequestView() as v if v.status == "active":
                medications.append((day(v.authored_on) or "", v.ref))
            case AllergyIntoleranceView() as v:
                allergies.append((day(v.recorded_date) or "", v.ref))
            case EncounterView() as v:
                visits.append((day(v.period.start) or "", v.ref))
            case ImmunizationView() as v if since <= (day(v.occurrence_date_time) or "") <= as_of:
                shots.append((day(v.occurrence_date_time) or "", v.ref))
            case _:
                pass
    return [
        *_newest_first(problems),
        *_newest_first(medications),
        *_newest_first(allergies),
        *_newest_first(visits)[:RECENT_VISITS],
        *_newest_first(shots),
    ]


def _newest_first(items: list[tuple[str, str]]) -> list[str]:
    return [ref for _, ref in sorted(items, reverse=True)]
