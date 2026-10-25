"""Render indexed resources as short text cards (PLAN.md D4).

One card per resource, except clinical notes, which become one card per
chunk. A card's id is the FHIR reference ("Observation/<id>"), with "#<n>"
added for note chunks, so every citation maps back to a resource a clinician
can open. Cards keep the facts (names, values, units, dates, status, codes)
and drop JSON noise such as profile URLs and identifiers.

`series_key` groups repeated measurements of the same thing (all HbA1c
results, all prescriptions of one drug). The retriever uses it to pull in
the newest members of a series (fhir_rag.retrieval.retriever).
"""

from collections.abc import Mapping
from dataclasses import dataclass

from fhir_rag.fhir.loader import Resource
from fhir_rag.fhir.notes import note_text, split_note
from fhir_rag.fhir.views import (
    AllergyIntoleranceView,
    CarePlanView,
    CodeableConcept,
    ConditionView,
    DeviceView,
    DiagnosticReportView,
    DocumentReferenceView,
    EncounterView,
    ImagingStudyView,
    ImmunizationView,
    MedicationRequestView,
    ObservationView,
    PatientView,
    ProcedureView,
    ResourceView,
    day,
    parse_view,
)

CARD_VERSION = "1"  # bump when card text changes, so reports show it


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    resource_ref: str
    resource_type: str
    date: str | None
    text: str
    series_key: str | None = None


def _join(*parts: str | None) -> str:
    return " | ".join(p for p in parts if p)


def _reasons(refs: list[str]) -> str | None:
    return "reason: " + "; ".join(refs) if refs else None


def _code(concept: CodeableConcept) -> str | None:
    return concept.code_tag or None


def _series(view: ResourceView, concept: CodeableConcept | None) -> str | None:
    if concept is None or not concept.code_tag:
        return None
    return f"{view.resource_type}|{concept.code_tag}"


def _observation_value(obs: ObservationView) -> str:
    if obs.component:
        parts = [f"{c.code.label} {c.value_text()}".strip() for c in obs.component]
        return "; ".join(p for p in parts if p)
    return obs.value_text()


def _lab_results(report: DiagnosticReportView, lookup: Mapping[str, Resource]) -> str:
    results = []
    for ref in report.result:
        target = lookup.get(ref.target_id or "")
        if target is None:
            continue
        obs = ObservationView.model_validate(target)
        results.append(f"{obs.code.label} {_observation_value(obs)}".strip())
    return "results: " + "; ".join(results) if results else ""


def chunks_for(resource: Resource, lookup: Mapping[str, Resource]) -> list[Chunk]:
    """Cards for one resource; [] for types that aren't indexed.

    lookup maps resource ids in the same bundle to resources, for
    DiagnosticReport results.
    """
    view = parse_view(resource)
    if view is None:
        return []

    def card(date: str | None, text: str, series: str | None = None) -> list[Chunk]:
        return [Chunk(view.ref, view.ref, view.resource_type, date, text, series)]

    match view:
        case PatientView():
            deceased = day(view.deceased_date_time)
            return card(
                day(view.birth_date),
                _join(
                    "Patient",
                    f"born {view.birth_date}",
                    view.display_name,
                    f"gender {view.gender}" if view.gender else None,
                    f"deceased {deceased}" if deceased else None,
                ),
            )
        case ConditionView():
            onset = day(view.onset_date_time)
            resolved = day(view.abatement_date_time)
            return card(
                onset,
                _join(
                    "Condition",
                    f"onset {onset}" if onset else None,
                    view.code.label,
                    f"clinical status {view.status}" if view.status else None,
                    f"resolved {resolved}" if resolved else None,
                    _code(view.code),
                ),
                _series(view, view.code),
            )
        case ObservationView():
            date = day(view.effective_date_time)
            category = view.category_code
            return card(
                date,
                _join(
                    f"Observation ({category})" if category else "Observation",
                    date,
                    f"{view.code.label} = {_observation_value(view)}",
                    f"status {view.status}" if view.status else None,
                    _code(view.code),
                ),
                _series(view, view.code),
            )
        case MedicationRequestView():
            date = day(view.authored_on)
            concept = view.medication_codeable_concept
            return card(
                date,
                _join(
                    "MedicationRequest",
                    f"prescribed {date}" if date else None,
                    view.medication,
                    f"status {view.status}" if view.status else None,
                    _reasons([r.display or "" for r in view.reason_reference if r.display]),
                    _code(concept) if concept else None,
                ),
                _series(view, concept),
            )
        case AllergyIntoleranceView():
            date = day(view.recorded_date)
            reactions = [m.label for r in view.reaction for m in r.manifestation if m.label]
            status = view.clinical_status.label if view.clinical_status else ""
            if not status and view.clinical_status and view.clinical_status.coding:
                status = view.clinical_status.coding[0].code or ""
            return card(
                date,
                _join(
                    "AllergyIntolerance",
                    f"recorded {date}" if date else None,
                    view.code.label,
                    ", ".join(
                        x
                        for x in [
                            view.type,
                            "category " + "/".join(view.category) if view.category else None,
                            f"criticality {view.criticality}" if view.criticality else None,
                        ]
                        if x
                    ),
                    f"clinical status {status}" if status else None,
                    "reactions: " + "; ".join(reactions) if reactions else None,
                    _code(view.code),
                ),
            )
        case ImmunizationView():
            date = day(view.occurrence_date_time)
            return card(
                date,
                _join(
                    "Immunization",
                    date,
                    view.vaccine_code.label,
                    f"status {view.status}" if view.status else None,
                    _code(view.vaccine_code),
                ),
                _series(view, view.vaccine_code),
            )
        case ProcedureView():
            date = day(view.performed)
            return card(
                date,
                _join(
                    "Procedure",
                    date,
                    view.code.label,
                    f"status {view.status}" if view.status else None,
                    _reasons([r.display or "" for r in view.reason_reference if r.display]),
                    _code(view.code),
                ),
                _series(view, view.code),
            )
        case EncounterView():
            date = day(view.period.start)
            kind = view.type[0] if view.type else CodeableConcept()
            return card(
                date,
                _join(
                    "Encounter",
                    date,
                    kind.label,
                    f"class {view.class_.code}" if view.class_ and view.class_.code else None,
                    _reasons([c.label for c in view.reason_code if c.label]),
                    f"at {view.service_provider.display}"
                    if view.service_provider and view.service_provider.display
                    else None,
                ),
            )
        case DiagnosticReportView():
            if view.is_note:
                return []  # indexed once, from DocumentReference
            date = day(view.effective_date_time)
            return card(
                date,
                _join(
                    "DiagnosticReport",
                    date,
                    view.code.label,
                    _lab_results(view, lookup),
                    _code(view.code),
                ),
                _series(view, view.code),
            )
        case DocumentReferenceView():
            date = day(view.date)
            parts = split_note(note_text(resource))
            return [
                Chunk(
                    f"{view.ref}#{i}",
                    view.ref,
                    view.resource_type,
                    date,
                    _join("Clinical note", date, f"part {i} of {len(parts)}", text),
                )
                for i, text in enumerate(parts, start=1)
            ]
        case CarePlanView():
            date = day(view.period.start)
            end = day(view.period.end)
            activities = [
                a.detail.code.label for a in view.activity if a.detail and a.detail.code.label
            ]
            return card(
                date,
                _join(
                    "CarePlan",
                    f"{date} to {end}" if end else f"started {date}",
                    view.title,
                    f"status {view.status}" if view.status else None,
                    _reasons([r.display or "" for r in view.addresses if r.display]),
                    "activities: " + "; ".join(activities) if activities else None,
                ),
            )
        case DeviceView():
            date = day(view.manufacture_date)
            return card(
                date,
                _join(
                    "Device",
                    view.type.label,
                    f"status {view.status}" if view.status else None,
                    f"manufactured {date}" if date else None,
                    _code(view.type),
                ),
            )
        case ImagingStudyView():
            date = day(view.started)
            procedure = view.procedure_code[0] if view.procedure_code else CodeableConcept()
            return card(
                date,
                _join(
                    "ImagingStudy",
                    date,
                    procedure.label,
                    f"status {view.status}" if view.status else None,
                ),
            )
    return []
