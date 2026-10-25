"""Generate template questions with gold labels computed from the raw bundles.

This module parses FHIR on its own, with plain dict access, and imports
nothing from the service except the bundle loader (PLAN.md D12). If the
service's views or cards misread a field, the labels here won't share the
mistake, and the eval will show it.

Every question's gold evidence is listed as groups (see questions.py).
"""

import hashlib
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

from fhir_rag.evals.questions import Category, Question
from fhir_rag.fhir.loader import Bundle, iter_resources

AS_OF = "2026-10-01"  # Synthea -e end date; questions about "the last year" use it

LOINC = "http://loinc.org"
SNOMED = "http://snomed.info/sct"
CVX = "http://hl7.org/fhir/sid/cvx"

# Labs and vitals asked about by name, in the words a clinician would use.
LAB_NAMES = {
    "4548-4": "hemoglobin A1c",
    "2339-0": "blood glucose",
    "2093-3": "total cholesterol",
    "18262-6": "LDL cholesterol",
    "2085-9": "HDL cholesterol",
    "2571-8": "triglycerides",
    "38483-4": "creatinine",
    "718-7": "hemoglobin",
    "6298-4": "potassium",
    "2947-0": "sodium",
}
LABS_PER_PATIENT = 2
BLOOD_PRESSURE = "85354-9"
FLU_VACCINE = "140"
HBA1C = "4548-4"
SMOKING_STATUS = "72166-2"
LIPID_PANEL = "57698-3"
TOTAL_CHOLESTEROL = "2093-3"
COLONOSCOPY = "73761001"
# Tests Synthea never generates: questions about them can't be answered.
NEVER_RECORDED = {
    "882-1": "What is the patient's blood type?",
    "20447-9": "What was the patient's most recent HIV viral load?",
}


@dataclass(frozen=True)
class LayTerm:
    phrase: str  # what the question says
    codes: frozenset[str]  # SNOMED codes that count as a match
    matches: tuple[str, ...]  # display substrings that rule out a "never diagnosed" question
    chronic: bool  # only chronic conditions are used for "not in record" questions


LAY_TERMS = [
    LayTerm("high blood pressure", frozenset({"59621000"}), ("hypertension",), True),
    LayTerm("type 2 diabetes", frozenset({"44054006"}), ("diabetes",), True),
    LayTerm(
        "high cholesterol",
        frozenset({"55822004"}),
        ("hyperlipidemia", "cholesterol"),
        True,
    ),
    LayTerm(
        "heart disease",
        frozenset({"414545008"}),
        ("heart", "myocardial", "coronary"),
        True,
    ),
    LayTerm(
        "a heart attack",
        frozenset({"22298006", "401314000", "401303003"}),
        ("myocardial infarction",),
        True,
    ),
    LayTerm(
        "kidney disease",
        frozenset({"431855005", "431856006", "433144002", "431857002"}),
        ("kidney",),
        True,
    ),
    LayTerm(
        "borderline diabetes",
        frozenset({"714628002"}),
        ("prediabetes", "diabetes"),
        True,
    ),
    LayTerm("obesity", frozenset({"162864005"}), ("obesity",), True),
    LayTerm("a low red blood cell count", frozenset({"271737000"}), ("anemia",), True),
    LayTerm(
        "a sinus infection",
        frozenset({"444814009", "40055000", "75498004"}),
        ("sinusitis",),
        False,
    ),
    LayTerm(
        "a sore throat infection",
        frozenset({"195662009"}),
        ("pharyngitis", "sore throat"),
        False,
    ),
    LayTerm("a chest cold", frozenset({"10509002"}), ("bronchitis",), False),
    LayTerm("a bladder infection", frozenset({"307426000"}), ("cystitis",), False),
    LayTerm("gum disease", frozenset({"66383009"}), ("gingivitis", "periodontal"), False),
]
LAY_POSITIVES_PER_PATIENT = 2
PRESCRIBED_FOR_PER_PATIENT = 2


def _ref(r: dict[str, Any]) -> str:
    return f"{r['resourceType']}/{r['id']}"


def _first_code(concept: dict[str, Any] | None, system: str | None = None) -> str | None:
    for coding in (concept or {}).get("coding", []):
        if system is None or coding.get("system") == system:
            code: str | None = coding.get("code")
            return code
    return None


def _label(concept: dict[str, Any] | None) -> str:
    concept = concept or {}
    text: str = concept.get("text") or next(
        (c.get("display", "") for c in concept.get("coding", [])), ""
    )
    return text


def _plain(display: str) -> str:
    """'Essential hypertension (disorder)' -> 'essential hypertension'."""
    return display.split(" (")[0].lower()


def _num(value: float) -> str:
    return f"{value:g}"


def _order(patient_id: str, key: str) -> str:
    """Per-patient stable pseudo-random order, so patients get different picks."""
    return hashlib.sha256(f"{patient_id}:{key}".encode()).hexdigest()


class _Builder:
    def __init__(self, patient_id: str, resources: list[dict[str, Any]]):
        self.pid = patient_id
        self.by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for r in resources:
            self.by_type[r["resourceType"]].append(r)
        self.out: list[Question] = []

    def add(
        self,
        slug: str,
        category: Category,
        text: str,
        groups: list[list[str]],
        key_facts: Iterable[str] = (),
        note: str = "",
    ) -> None:
        self.out.append(
            Question(
                id=f"{slug}:{self.pid[:8]}",
                patient_id=self.pid,
                question=text,
                category=category,
                gold_groups=[sorted(g) for g in groups],
                key_facts=list(key_facts),
                source="template",
                note=note,
            )
        )

    # --- fact lookup ---

    def current_medications(self) -> None:
        by_drug: dict[str, list[str]] = defaultdict(list)
        for r in self.by_type["MedicationRequest"]:
            if r.get("status") == "active":
                by_drug[_label(r.get("medicationCodeableConcept"))].append(_ref(r))
        if by_drug:
            self.add(
                "current-meds",
                "fact_lookup",
                "What medications is the patient currently prescribed?",
                [by_drug[d] for d in sorted(by_drug)],
                note="active MedicationRequests, one group per drug",
            )

    def active_problems(self) -> None:
        refs = [
            _ref(r)
            for r in self.by_type["Condition"]
            if _first_code(r.get("clinicalStatus")) == "active"
            and _label(r.get("code")).endswith("(disorder)")
        ]
        if refs:
            self.add(
                "active-problems",
                "fact_lookup",
                "What active diagnoses does the patient have?",
                [[ref] for ref in sorted(refs)],
                note="active Conditions whose SNOMED display ends in (disorder)",
            )

    def allergies(self) -> None:
        refs = [_ref(r) for r in self.by_type["AllergyIntolerance"]]
        if refs:
            self.add(
                "allergies",
                "fact_lookup",
                "What allergies are documented for this patient?",
                [[ref] for ref in sorted(refs)],
            )

    def recent_vaccines(self) -> None:
        start = f"{int(AS_OF[:4]) - 1}{AS_OF[4:]}"
        refs = [
            _ref(r)
            for r in self.by_type["Immunization"]
            if start <= r.get("occurrenceDateTime", "")[:10] <= AS_OF
        ]
        if refs:
            self.add(
                "vaccines-last-year",
                "fact_lookup",
                "Which vaccines did the patient receive in the last year?",
                [[ref] for ref in sorted(refs)],
                note=f"Immunizations dated {start} to {AS_OF}",
            )

    def smoking_status(self) -> None:
        latest = self._latest_observation(SMOKING_STATUS)
        if latest is not None:
            self.add(
                "smoking-status",
                "fact_lookup",
                "Does the patient smoke?",
                [[_ref(latest)]],
                note="latest Tobacco smoking status observation",
            )

    # --- values and dates ---

    def _latest_observation(self, code: str) -> dict[str, Any] | None:
        matches = [
            r for r in self.by_type["Observation"] if _first_code(r.get("code"), LOINC) == code
        ]
        return max(matches, key=lambda r: r.get("effectiveDateTime", ""), default=None)

    def latest_labs(self) -> None:
        present = [c for c in LAB_NAMES if self._latest_observation(c) is not None]
        for code in sorted(present, key=lambda c: _order(self.pid, c))[:LABS_PER_PATIENT]:
            obs = self._latest_observation(code)
            assert obs is not None
            value = obs.get("valueQuantity", {}).get("value")
            if value is None:
                continue
            day = obs["effectiveDateTime"][:10]
            self.add(
                f"latest-lab-{code}",
                "values_dates",
                f"What was the patient's most recent {LAB_NAMES[code]} result, "
                "and when was it measured?",
                [[_ref(obs)]],
                [_num(value), day],
            )

    def latest_blood_pressure(self) -> None:
        obs = self._latest_observation(BLOOD_PRESSURE)
        if obs is None:
            return
        values = {
            _first_code(c.get("code"), LOINC): c.get("valueQuantity", {}).get("value")
            for c in obs.get("component", [])
        }
        systolic, diastolic = values.get("8480-6"), values.get("8462-4")
        if systolic is None or diastolic is None:
            return
        self.add(
            "latest-bp",
            "values_dates",
            "What was the patient's most recent blood pressure reading?",
            [[_ref(obs)]],
            [_num(systolic), _num(diastolic), obs["effectiveDateTime"][:10]],
        )

    def latest_lipid_panel(self) -> None:
        reports = [
            r
            for r in self.by_type["DiagnosticReport"]
            if _first_code(r.get("code"), LOINC) == LIPID_PANEL
        ]
        latest = max(reports, key=lambda r: r.get("effectiveDateTime", ""), default=None)
        if latest is None:
            return
        results = {ref["reference"].removeprefix("urn:uuid:") for ref in latest.get("result", [])}
        members = [r for r in self.by_type["Observation"] if r["id"] in results]
        cholesterol = next(
            (
                r["valueQuantity"]["value"]
                for r in members
                if _first_code(r.get("code"), LOINC) == TOTAL_CHOLESTEROL
            ),
            None,
        )
        facts = [latest["effectiveDateTime"][:10]]
        if cholesterol is not None:
            facts.insert(0, _num(cholesterol))
        self.add(
            "latest-lipid-panel",
            "values_dates",
            "What did the patient's most recent lipid panel show?",
            [[_ref(latest), *(_ref(r) for r in members)]],
            facts,
            note="the report or any of its result observations counts",
        )

    def last_colonoscopy(self) -> None:
        done = [
            r
            for r in self.by_type["Procedure"]
            if _first_code(r.get("code"), SNOMED) == COLONOSCOPY
        ]
        if not done:
            self.add(
                "never-colonoscopy",
                "not_in_record",
                "When was the patient's most recent colonoscopy?",
                [],
                note=f"no Procedure with SNOMED {COLONOSCOPY}",
            )
            return
        latest = max(done, key=lambda r: r.get("performedPeriod", {}).get("start", ""))
        self.add(
            "last-colonoscopy",
            "values_dates",
            "When was the patient's most recent colonoscopy?",
            [[_ref(latest)]],
            [latest["performedPeriod"]["start"][:10]],
        )

    def last_flu_shot(self) -> None:
        shots = [
            r
            for r in self.by_type["Immunization"]
            if _first_code(r.get("vaccineCode"), CVX) == FLU_VACCINE
        ]
        latest = max(shots, key=lambda r: r.get("occurrenceDateTime", ""), default=None)
        if latest is not None:
            self.add(
                "last-flu-shot",
                "values_dates",
                "When did the patient last get a flu shot?",
                [[_ref(latest)]],
                [latest["occurrenceDateTime"][:10]],
            )

    def last_visit(self) -> None:
        latest = max(
            self.by_type["Encounter"],
            key=lambda r: r["period"].get("start", ""),
            default=None,
        )
        if latest is not None:
            self.add(
                "last-visit",
                "values_dates",
                "When was the patient's most recent visit, and what kind of visit was it?",
                [[_ref(latest)]],
                [latest["period"]["start"][:10]],
            )

    # --- lay terms ---

    def lay_terms(self) -> None:
        conditions = self.by_type["Condition"]
        positives = []
        for term in LAY_TERMS:
            refs = [r for r in conditions if _first_code(r.get("code"), SNOMED) in term.codes]
            if refs:
                positives.append((term, refs))
        positives.sort(key=lambda pair: _order(self.pid, pair[0].phrase))
        for term, refs in positives[:LAY_POSITIVES_PER_PATIENT]:
            first = min(r.get("onsetDateTime", "") for r in refs)[:10]
            self.add(
                f"lay-{term.phrase.replace(' ', '-')}",
                "lay_terms",
                f"Has the patient ever been diagnosed with {term.phrase}? If so, when?",
                [[_ref(r) for r in refs]],
                [first],
                note=f"Conditions with SNOMED {sorted(term.codes)}",
            )

        # One "never diagnosed" question: a chronic condition with no trace in
        # any Condition display.
        displays = " ".join(_label(r.get("code")).lower() for r in conditions)
        absent = [t for t in LAY_TERMS if t.chronic and not any(m in displays for m in t.matches)]
        if absent:
            term = min(absent, key=lambda t: _order(self.pid, "absent:" + t.phrase))
            self.add(
                f"never-{term.phrase.replace(' ', '-')}",
                "not_in_record",
                f"Has the patient ever been diagnosed with {term.phrase}?",
                [],
                note=f"no Condition display contains any of {list(term.matches)}",
            )

    # --- multi-step ---

    def prescribed_for(self) -> None:
        by_reason: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
        for r in self.by_type["MedicationRequest"]:
            for reason in r.get("reasonReference", []):
                display = reason.get("display")
                if display:
                    drug = _label(r.get("medicationCodeableConcept"))
                    by_reason[display][drug].append(_ref(r))
        reasons = sorted(by_reason, key=lambda d: (-sum(map(len, by_reason[d].values())), d))
        for display in reasons[:PRESCRIBED_FOR_PER_PATIENT]:
            drugs = by_reason[display]
            self.add(
                f"prescribed-for-{_plain(display).replace(' ', '-')}",
                "multi_step",
                f"Which medications have been prescribed for the patient's {_plain(display)}?",
                [drugs[d] for d in sorted(drugs)],
                note="MedicationRequests whose reasonReference names the condition; "
                "one group per drug",
            )

    def a1c_trend(self) -> None:
        results = sorted(
            (r for r in self.by_type["Observation"] if _first_code(r.get("code"), LOINC) == HBA1C),
            key=lambda r: r.get("effectiveDateTime", ""),
        )[-3:]
        if len(results) == 3:
            self.add(
                "a1c-trend",
                "multi_step",
                "How have the patient's last three hemoglobin A1c results changed?",
                [[_ref(r)] for r in results],
                [_num(r["valueQuantity"]["value"]) for r in results],
                note="each of the three latest HbA1c results is its own group",
            )

    def last_er_visit(self) -> None:
        visits = [
            r
            for r in self.by_type["Encounter"]
            if r.get("class", {}).get("code") == "EMER" and r.get("reasonCode")
        ]
        latest = max(visits, key=lambda r: r["period"].get("start", ""), default=None)
        if latest is not None:
            self.add(
                "last-er-visit",
                "multi_step",
                "Why was the patient last seen in the emergency department, and when?",
                [[_ref(latest)]],
                [latest["period"]["start"][:10]],
                note="latest EMER Encounter that has a reasonCode",
            )

    # --- not in record ---

    def never_recorded(self) -> None:
        codes = sorted(NEVER_RECORDED, key=lambda c: _order(self.pid, "never:" + c))
        code = codes[0]
        if self._latest_observation(code) is None:
            self.add(
                f"never-recorded-{code}",
                "not_in_record",
                NEVER_RECORDED[code],
                [],
                note=f"Synthea doesn't generate LOINC {code}",
            )

    def missing_lab(self) -> None:
        absent = [c for c in LAB_NAMES if self._latest_observation(c) is None]
        if absent:
            code = min(absent, key=lambda c: _order(self.pid, "missing:" + c))
            self.add(
                f"missing-lab-{code}",
                "not_in_record",
                f"What was the patient's most recent {LAB_NAMES[code]} result?",
                [],
                note=f"no Observation with LOINC {code}",
            )


def template_questions(patient_id: str, bundle: Bundle) -> list[Question]:
    """All template questions for one patient bundle."""
    builder = _Builder(patient_id, list(iter_resources(bundle)))
    builder.current_medications()
    builder.active_problems()
    builder.allergies()
    builder.recent_vaccines()
    builder.smoking_status()
    builder.latest_labs()
    builder.latest_blood_pressure()
    builder.latest_lipid_panel()
    builder.last_colonoscopy()
    builder.last_flu_shot()
    builder.last_visit()
    builder.lay_terms()
    builder.prescribed_for()
    builder.a1c_trend()
    builder.last_er_visit()
    builder.missing_lab()
    builder.never_recorded()
    return builder.out
