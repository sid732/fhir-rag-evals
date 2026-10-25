from typing import Any

from cohort import patient_one

from fhir_rag.fhir.cards import chunks_for
from fhir_rag.fhir.notes import split_note
from fhir_rag.fhir.views import (
    CarePlanView,
    CodeableConcept,
    ConditionView,
    ObservationView,
    Reference,
    parse_view,
)


def _by_id(resources: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {r["id"]: r for r in resources}


def test_reference_target_ids() -> None:
    assert Reference(reference="urn:uuid:abc").target_id == "abc"
    assert Reference(reference="Patient/abc").target_id == "abc"
    conditional = "Practitioner?identifier=http://hl7.org/fhir/sid/us-npi|999"
    assert Reference(reference=conditional).target_id is None


def test_codeable_concept_label_falls_back_to_coding() -> None:
    concept = CodeableConcept.model_validate({"coding": [{"code": "x", "display": "Shown"}]})
    assert concept.label == "Shown"
    assert CodeableConcept.model_validate({"coding": [{"code": "x"}]}).label == "x"
    assert CodeableConcept().label == ""


def test_value_choice_types() -> None:
    quantity = ObservationView.model_validate(
        {"resourceType": "Observation", "id": "o", "valueQuantity": {"value": 6.80, "unit": "%"}}
    )
    assert quantity.value_text() == "6.8 %"
    coded = ObservationView.model_validate(
        {
            "resourceType": "Observation",
            "id": "o",
            "valueCodeableConcept": {"text": "Never smoked tobacco (finding)"},
        }
    )
    assert coded.value_text() == "Never smoked tobacco (finding)"
    text = ObservationView.model_validate(
        {"resourceType": "Observation", "id": "o", "valueString": "Positive"}
    )
    assert text.value_text() == "Positive"


def test_condition_status_and_unknown_fields_ignored() -> None:
    view = ConditionView.model_validate(
        {"resourceType": "Condition", "id": "c", "clinicalStatus": {"coding": []}, "brandNew": 1}
    )
    assert view.status == ""
    assert view.ref == "Condition/c"


def test_careplan_title_skips_the_generic_category() -> None:
    plan = CarePlanView.model_validate(
        {
            "resourceType": "CarePlan",
            "id": "cp",
            "category": [
                {"coding": [{"code": "assess-plan"}]},
                {
                    "coding": [{"code": "1", "display": "Diabetes self management plan"}],
                    "text": "Diabetes self management plan",
                },
            ],
        }
    )
    assert plan.title == "Diabetes self management plan"


def test_unindexed_types_have_no_view_or_cards() -> None:
    claim = {"resourceType": "Claim", "id": "c1"}
    assert parse_view(claim) is None
    assert chunks_for(claim, {}) == []


def test_observation_card_has_value_date_code_and_series() -> None:
    resources = patient_one()
    [card] = chunks_for(_by_id(resources)["p1-a1c-2026"], _by_id(resources))
    assert card.chunk_id == card.resource_ref == "Observation/p1-a1c-2026"
    assert card.date == "2026-03-04"
    assert "Hemoglobin A1c/Hemoglobin.total in Blood = 6.8 %" in card.text
    assert "LOINC 4548-4" in card.text
    assert card.series_key == "Observation|LOINC 4548-4"


def test_blood_pressure_components_are_rendered() -> None:
    resources = patient_one()
    [card] = chunks_for(_by_id(resources)["p1-bp"], _by_id(resources))
    assert "Diastolic Blood Pressure 82 mm[Hg]" in card.text
    assert "Systolic Blood Pressure 128 mm[Hg]" in card.text


def test_lab_report_lists_its_results() -> None:
    resources = patient_one()
    [card] = chunks_for(_by_id(resources)["p1-lipids"], _by_id(resources))
    assert "results: Cholesterol [Mass/volume] in Serum or Plasma 190 mg/dL" in card.text


def test_note_reports_are_skipped_because_document_reference_has_the_note() -> None:
    resources = patient_one()
    assert chunks_for(_by_id(resources)["p1-note-report"], _by_id(resources)) == []
    chunks = chunks_for(_by_id(resources)["p1-note"], _by_id(resources))
    assert [c.chunk_id for c in chunks] == ["DocumentReference/p1-note#1"]
    assert chunks[0].resource_ref == "DocumentReference/p1-note"
    assert "Recheck blood pressure." in chunks[0].text


def test_medication_card_names_the_reason() -> None:
    resources = patient_one()
    [card] = chunks_for(_by_id(resources)["p1-lisinopril"], _by_id(resources))
    assert "reason: Essential hypertension (disorder)" in card.text
    assert "status active" in card.text


def test_split_note_packs_whole_sections() -> None:
    text = "# A\none two\n\n# B\nthree four five\n\n# C\nsix"
    assert split_note(text, max_words=6) == ["# A one two", "# B three four five", "# C six"]


def test_split_note_breaks_an_oversized_section() -> None:
    words = " ".join(f"w{i}" for i in range(10))
    assert split_note(f"# Long\n{words}", max_words=4) == [
        "# Long w0 w1",
        "w2 w3 w4 w5",
        "w6 w7 w8 w9",
    ]
