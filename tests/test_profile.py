import base64
from typing import Any

from fhir_rag.tools.profile import (
    CODE_FIELDS,
    CodeCount,
    CohortProfile,
    TypeStats,
    build_profile,
    note_text,
    render_markdown,
    top_codes,
    type_stats,
)

LOINC = "http://loinc.org"
A1C = "Hemoglobin A1c/Hemoglobin.total in Blood"


def _bundle(*resources: dict[str, Any]) -> dict[str, Any]:
    entries = [{"resource": r} for r in resources]
    return {"resourceType": "Bundle", "type": "transaction", "entry": entries}


def _observation(id_: str, code: str, display: str) -> dict[str, Any]:
    coding = {"system": LOINC, "code": code, "display": display}
    return {"resourceType": "Observation", "id": id_, "code": {"coding": [coding]}}


def _note(id_: str, text: str) -> dict[str, Any]:
    data = base64.b64encode(text.encode()).decode()
    attachment = {"contentType": "text/plain; charset=utf-8", "data": data}
    return {
        "resourceType": "DocumentReference",
        "id": id_,
        "content": [{"attachment": attachment}],
    }


def test_type_stats_counts_and_compact_json_bytes() -> None:
    claim = {"resourceType": "Claim", "id": "c1"}  # 34 bytes as compact JSON
    patient = {"resourceType": "Patient", "id": "p1"}  # 36 bytes
    bundles = [_bundle(claim, patient), _bundle({"resourceType": "Claim", "id": "c2"})]
    assert type_stats(bundles) == [
        TypeStats("Claim", 2, 68),
        TypeStats("Patient", 1, 36),
    ]


def test_type_stats_breaks_byte_ties_by_type_name() -> None:
    bundle = _bundle({"resourceType": "Group", "id": "g1"}, {"resourceType": "Claim", "id": "c1"})
    assert [s.resource_type for s in type_stats([bundle])] == ["Claim", "Group"]


def test_note_text_decodes_the_base64_attachment() -> None:
    text = "Chief complaint: cough.\nPlan: rest."
    assert note_text(_note("d1", text)) == text


def test_note_text_without_inline_data_is_empty() -> None:
    by_url = {"attachment": {"url": "https://example.org/notes/1"}}
    assert note_text({"resourceType": "DocumentReference", "id": "d1", "content": [by_url]}) == ""
    assert note_text({"resourceType": "DocumentReference", "id": "d2"}) == ""


def test_top_codes_most_common_first_and_ties_by_code() -> None:
    snomed = {
        "system": "http://snomed.info/sct",
        "code": "44054006",
        "display": "Diabetes",
    }
    bundle = _bundle(
        _observation("o1", "4548-4", A1C),
        _observation("o2", "4548-4", A1C),
        _observation("o3", "8302-2", "Body Height"),
        _observation("o4", "29463-7", "Body Weight"),
        {"resourceType": "Observation", "id": "o5"},  # no code: skipped
        {"resourceType": "Condition", "id": "c1", "code": {"coding": [snomed]}},
    )
    assert top_codes([bundle], "Observation", "code", n=2) == [
        CodeCount(LOINC, "4548-4", A1C, 2),
        CodeCount(LOINC, "29463-7", "Body Weight", 1),  # "29463-7" sorts before "8302-2"
    ]


def test_build_profile() -> None:
    p1 = _bundle({"resourceType": "Patient", "id": "p1"}, _note("d1", "one two three"))
    p2 = _bundle(
        {"resourceType": "Patient", "id": "p2"},
        _note("d2", "one"),
        _observation("o1", "8302-2", "Body Height"),
    )
    profile = build_profile([p1, p2], top_n=5)
    assert profile.patients == 2
    assert profile.resources_per_patient == [2, 3]
    assert profile.note_words == [3, 1]
    assert list(profile.top_codes) == list(CODE_FIELDS)
    assert profile.top_codes["Observation"] == [CodeCount(LOINC, "8302-2", "Body Height", 1)]
    assert profile.top_codes["Condition"] == []


def test_render_markdown_tables_and_summaries() -> None:
    profile = CohortProfile(
        patients=3,
        resources_per_patient=[10, 20, 30],
        types=[TypeStats("Claim", 2, 1_500_000), TypeStats("Patient", 1, 500_000)],
        note_words=[100, 250, 400],
        top_codes={"Observation": [CodeCount(LOINC, "4548-4", A1C, 3)]},
    )
    md = render_markdown(profile)
    assert "Patients: 3" in md
    assert "Resources per patient: min 10, median 20, max 30" in md
    assert "| Type | Count | Bytes | Share |" in md
    assert "| Claim | 2 | 1,500,000 | 75.0% |" in md
    assert "| Patient | 1 | 500,000 | 25.0% |" in md
    assert md.index("| Claim |") < md.index("| Patient |")
    assert "Note length (words): min 100, median 250, max 400" in md
    assert "### Observation" in md
    assert f"| 4548-4 | {A1C} | 3 |" in md
