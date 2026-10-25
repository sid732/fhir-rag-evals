"""Builders for a tiny two-patient cohort shaped like Synthea output."""

import base64
from typing import Any

LOINC = "http://loinc.org"
SNOMED = "http://snomed.info/sct"
RXNORM = "http://www.nlm.nih.gov/research/umls/rxnorm"
AS_OF = "2026-10-01"
P1, P2 = "p1", "p2"


def concept(system: str, code: str, display: str) -> dict[str, Any]:
    return {"coding": [{"system": system, "code": code, "display": display}], "text": display}


def ref(rid: str) -> dict[str, str]:
    return {"reference": f"urn:uuid:{rid}"}


def condition(
    rid: str, pid: str, code: str, display: str, onset: str, status: str
) -> dict[str, Any]:
    return {
        "resourceType": "Condition",
        "id": rid,
        "clinicalStatus": {"coding": [{"code": status}]},
        "code": concept(SNOMED, code, display),
        "subject": ref(pid),
        "onsetDateTime": f"{onset}T09:00:00-04:00",
    }


def observation(
    rid: str, pid: str, code: str, display: str, value: float, unit: str, date: str
) -> dict[str, Any]:
    return {
        "resourceType": "Observation",
        "id": rid,
        "status": "final",
        "category": [{"coding": [{"code": "laboratory"}]}],
        "code": concept(LOINC, code, display),
        "subject": ref(pid),
        "effectiveDateTime": f"{date}T09:00:00-04:00",
        "valueQuantity": {"value": value, "unit": unit},
    }


def med(
    rid: str, pid: str, code: str, name: str, date: str, status: str, reason: str | None
) -> dict[str, Any]:
    r: dict[str, Any] = {
        "resourceType": "MedicationRequest",
        "id": rid,
        "status": status,
        "medicationCodeableConcept": concept(RXNORM, code, name),
        "subject": ref(pid),
        "authoredOn": f"{date}T09:00:00-04:00",
    }
    if reason:
        r["reasonReference"] = [{"reference": "urn:uuid:x", "display": reason}]
    return r


def encounter(rid: str, pid: str, date: str, kind: str, cls: str = "AMB") -> dict[str, Any]:
    return {
        "resourceType": "Encounter",
        "id": rid,
        "status": "finished",
        "class": {"code": cls},
        "type": [concept(SNOMED, "185349003", kind)],
        "subject": ref(pid),
        "period": {"start": f"{date}T09:00:00-04:00", "end": f"{date}T09:30:00-04:00"},
    }


def note(rid: str, pid: str, date: str, text: str) -> dict[str, Any]:
    data = base64.b64encode(text.encode()).decode()
    return {
        "resourceType": "DocumentReference",
        "id": rid,
        "status": "current",
        "type": concept(LOINC, "34117-2", "History and physical note"),
        "subject": ref(pid),
        "date": f"{date}T09:00:00-04:00",
        "content": [{"attachment": {"contentType": "text/plain; charset=utf-8", "data": data}}],
    }


def patient_one() -> list[dict[str, Any]]:
    return [
        {
            "resourceType": "Patient",
            "id": P1,
            "name": [{"prefix": ["Mrs."], "given": ["Ana1"], "family": "Test2"}],
            "gender": "female",
            "birthDate": "1960-05-01",
        },
        condition(
            "p1-htn", P1, "59621000", "Essential hypertension (disorder)", "2015-03-01", "active"
        ),
        condition(
            "p1-sinus", P1, "444814009", "Viral sinusitis (disorder)", "2020-01-10", "resolved"
        ),
        med(
            "p1-lisinopril",
            P1,
            "314076",
            "lisinopril 10 MG Oral Tablet",
            "2026-06-01",
            "active",
            "Essential hypertension (disorder)",
        ),
        med(
            "p1-amox",
            P1,
            "308182",
            "amoxicillin 250 MG Oral Capsule",
            "2020-01-10",
            "completed",
            "Viral sinusitis (disorder)",
        ),
        observation(
            "p1-a1c-2024",
            P1,
            "4548-4",
            "Hemoglobin A1c/Hemoglobin.total in Blood",
            6.1,
            "%",
            "2024-03-01",
        ),
        observation(
            "p1-a1c-2025",
            P1,
            "4548-4",
            "Hemoglobin A1c/Hemoglobin.total in Blood",
            6.4,
            "%",
            "2025-03-01",
        ),
        observation(
            "p1-a1c-2026",
            P1,
            "4548-4",
            "Hemoglobin A1c/Hemoglobin.total in Blood",
            6.8,
            "%",
            "2026-03-04",
        ),
        observation(
            "p1-chol",
            P1,
            "2093-3",
            "Cholesterol [Mass/volume] in Serum or Plasma",
            190,
            "mg/dL",
            "2026-03-04",
        ),
        {
            "resourceType": "Observation",
            "id": "p1-bp",
            "status": "final",
            "category": [{"coding": [{"code": "vital-signs"}]}],
            "code": concept(LOINC, "85354-9", "Blood pressure panel with all children optional"),
            "subject": ref(P1),
            "effectiveDateTime": "2026-06-01T09:00:00-04:00",
            "component": [
                {
                    "code": concept(LOINC, "8462-4", "Diastolic Blood Pressure"),
                    "valueQuantity": {"value": 82, "unit": "mm[Hg]"},
                },
                {
                    "code": concept(LOINC, "8480-6", "Systolic Blood Pressure"),
                    "valueQuantity": {"value": 128, "unit": "mm[Hg]"},
                },
            ],
        },
        {
            "resourceType": "DiagnosticReport",
            "id": "p1-lipids",
            "status": "final",
            "code": concept(LOINC, "57698-3", "Lipid panel with direct LDL - Serum or Plasma"),
            "subject": ref(P1),
            "effectiveDateTime": "2026-03-04T09:00:00-04:00",
            "result": [ref("p1-chol")],
        },
        {
            "resourceType": "DiagnosticReport",
            "id": "p1-note-report",
            "status": "final",
            "code": concept(LOINC, "34117-2", "History and physical note"),
            "subject": ref(P1),
            "effectiveDateTime": "2026-06-01T09:00:00-04:00",
            "presentedForm": [{"contentType": "text/plain", "data": "eA=="}],
        },
        encounter("p1-enc-2023", P1, "2023-01-05", "General examination of patient (procedure)"),
        encounter("p1-enc-2024", P1, "2024-03-01", "General examination of patient (procedure)"),
        encounter("p1-enc-2025", P1, "2025-03-01", "General examination of patient (procedure)"),
        encounter("p1-enc-2026", P1, "2026-06-01", "Emergency room admission (procedure)", "EMER"),
        {
            "resourceType": "Immunization",
            "id": "p1-flu-2026",
            "status": "completed",
            "vaccineCode": concept(
                "http://hl7.org/fhir/sid/cvx", "140", "Influenza, seasonal, injectable"
            ),
            "patient": ref(P1),
            "occurrenceDateTime": "2026-01-15T09:00:00-05:00",
        },
        {
            "resourceType": "Immunization",
            "id": "p1-flu-2020",
            "status": "completed",
            "vaccineCode": concept(
                "http://hl7.org/fhir/sid/cvx", "140", "Influenza, seasonal, injectable"
            ),
            "patient": ref(P1),
            "occurrenceDateTime": "2020-01-15T09:00:00-05:00",
        },
        {
            "resourceType": "AllergyIntolerance",
            "id": "p1-allergy",
            "clinicalStatus": {"coding": [{"code": "active"}]},
            "type": "allergy",
            "category": ["medication"],
            "criticality": "low",
            "code": concept(SNOMED, "29046", "Lisinopril"),
            "patient": ref(P1),
            "recordedDate": "2019-04-01T09:00:00-04:00",
        },
        note(
            "p1-note",
            P1,
            "2026-06-01",
            "2026-06-01\n\n# Chief Complaint\nHeadache.\n\n# Plan\nRecheck blood pressure.",
        ),
        {"resourceType": "Claim", "id": "p1-claim", "patient": ref(P1)},
    ]


def patient_two() -> list[dict[str, Any]]:
    return [
        {
            "resourceType": "Patient",
            "id": P2,
            "name": [{"given": ["Bo3"], "family": "Other4"}],
            "birthDate": "1980-01-01",
        },
        condition(
            "p2-dm", P2, "44054006", "Diabetes mellitus type 2 (disorder)", "2018-02-02", "active"
        ),
        observation(
            "p2-a1c",
            P2,
            "4548-4",
            "Hemoglobin A1c/Hemoglobin.total in Blood",
            7.9,
            "%",
            "2026-02-02",
        ),
        encounter("p2-enc", P2, "2026-02-02", "General examination of patient (procedure)"),
    ]


def bundle(resources: list[dict[str, Any]]) -> dict[str, Any]:
    entries = [{"fullUrl": f"urn:uuid:{r['id']}", "resource": r} for r in resources]
    return {"resourceType": "Bundle", "type": "transaction", "entry": entries}
