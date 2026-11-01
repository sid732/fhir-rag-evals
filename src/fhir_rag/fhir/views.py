"""Typed views of the FHIR R4 resources the service indexes (design.md D2, D3).

Each view reads only the fields the cards and the gold labels need and
ignores everything else, so a Synthea upgrade that adds fields can't break
parsing. FHIR element names are camelCase; the views use snake_case and an
alias generator maps between them. Choice types such as `value[x]` appear as
one optional field per variant (value_quantity, value_string, ...) plus a
helper that returns whichever one is set.
"""

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from fhir_rag.fhir.loader import Resource


class FhirModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, extra="ignore", frozen=True
    )


class Coding(FhirModel):
    system: str | None = None
    code: str | None = None
    display: str | None = None


# Short names for the code systems that show up on cards.
SYSTEM_NAMES = {
    "http://loinc.org": "LOINC",
    "http://snomed.info/sct": "SNOMED",
    "http://www.nlm.nih.gov/research/umls/rxnorm": "RxNorm",
    "http://hl7.org/fhir/sid/cvx": "CVX",
    "http://hl7.org/fhir/sid/icd-10-cm": "ICD-10-CM",
}


class CodeableConcept(FhirModel):
    coding: list[Coding] = []
    text: str | None = None

    @property
    def label(self) -> str:
        """Human-readable name: text, else the first coding's display or code."""
        if self.text:
            return self.text
        for coding in self.coding:
            if coding.display or coding.code:
                return coding.display or coding.code or ""
        return ""

    @property
    def code_tag(self) -> str:
        """The first coding as "LOINC 4548-4", or "" when there is no code."""
        for coding in self.coding:
            if coding.code:
                name = SYSTEM_NAMES.get(coding.system or "", coding.system or "code")
                return f"{name} {coding.code}"
        return ""

    def has_code(self, system: str, code: str) -> bool:
        return any(c.system == system and c.code == code for c in self.coding)


class Reference(FhirModel):
    reference: str | None = None
    display: str | None = None

    @property
    def target_id(self) -> str | None:
        """Resource id for `urn:uuid:<id>` or `Type/<id>`; None for conditional refs."""
        ref = self.reference or ""
        if ref.startswith("urn:uuid:"):
            return ref.removeprefix("urn:uuid:")
        if "?" not in ref and ref.count("/") == 1:
            return ref.split("/")[1]
        return None


class Quantity(FhirModel):
    value: float | None = None
    unit: str | None = None

    def render(self) -> str:
        if self.value is None:
            return ""
        number = f"{self.value:g}"
        return f"{number} {self.unit}".strip() if self.unit else number


class Period(FhirModel):
    start: str | None = None
    end: str | None = None


class HumanName(FhirModel):
    prefix: list[str] = []
    given: list[str] = []
    family: str | None = None

    @property
    def full(self) -> str:
        return " ".join([*self.prefix, *self.given, self.family or ""]).strip()


def day(value: str | None) -> str | None:
    """The YYYY-MM-DD part of a FHIR date or dateTime."""
    return value[:10] if value else None


class ResourceView(FhirModel):
    resource_type: str
    id: str

    @property
    def ref(self) -> str:
        return f"{self.resource_type}/{self.id}"


class PatientView(ResourceView):
    name: list[HumanName] = []
    gender: str | None = None
    birth_date: str | None = None
    deceased_date_time: str | None = None

    @property
    def display_name(self) -> str:
        return self.name[0].full if self.name else ""


class ConditionView(ResourceView):
    clinical_status: CodeableConcept | None = None
    verification_status: CodeableConcept | None = None
    code: CodeableConcept = CodeableConcept()
    onset_date_time: str | None = None
    abatement_date_time: str | None = None

    @property
    def status(self) -> str:
        if self.clinical_status is None or not self.clinical_status.coding:
            return ""
        return self.clinical_status.coding[0].code or ""


class ValueChoice(FhirModel):
    """The `value[x]` variants Synthea uses on Observation and its components."""

    value_quantity: Quantity | None = None
    value_codeable_concept: CodeableConcept | None = None
    value_string: str | None = None

    def value_text(self) -> str:
        if self.value_quantity is not None:
            return self.value_quantity.render()
        if self.value_codeable_concept is not None:
            return self.value_codeable_concept.label
        return self.value_string or ""


class ObservationComponent(ValueChoice):
    code: CodeableConcept = CodeableConcept()


class ObservationView(ResourceView, ValueChoice):
    status: str | None = None
    category: list[CodeableConcept] = []
    code: CodeableConcept = CodeableConcept()
    effective_date_time: str | None = None
    component: list[ObservationComponent] = []

    @property
    def category_code(self) -> str:
        for concept in self.category:
            for coding in concept.coding:
                if coding.code:
                    return coding.code
        return ""


class MedicationRequestView(ResourceView):
    status: str | None = None
    medication_codeable_concept: CodeableConcept | None = None
    medication_reference: Reference | None = None
    authored_on: str | None = None
    reason_reference: list[Reference] = []

    @property
    def medication(self) -> str:
        if self.medication_codeable_concept is not None:
            return self.medication_codeable_concept.label
        if self.medication_reference is not None:
            return self.medication_reference.display or ""
        return ""


class Reaction(FhirModel):
    manifestation: list[CodeableConcept] = []
    severity: str | None = None


class AllergyIntoleranceView(ResourceView):
    clinical_status: CodeableConcept | None = None
    type: str | None = None
    category: list[str] = []
    criticality: str | None = None
    code: CodeableConcept = CodeableConcept()
    recorded_date: str | None = None
    reaction: list[Reaction] = []


class ImmunizationView(ResourceView):
    status: str | None = None
    vaccine_code: CodeableConcept = CodeableConcept()
    occurrence_date_time: str | None = None


class ProcedureView(ResourceView):
    status: str | None = None
    code: CodeableConcept = CodeableConcept()
    performed_date_time: str | None = None
    performed_period: Period | None = None
    reason_reference: list[Reference] = []

    @property
    def performed(self) -> str | None:
        if self.performed_date_time:
            return self.performed_date_time
        return self.performed_period.start if self.performed_period else None


class EncounterView(ResourceView):
    status: str | None = None
    class_: Annotated[Coding | None, Field(alias="class")] = None
    type: list[CodeableConcept] = []
    period: Period = Period()
    reason_code: list[CodeableConcept] = []
    service_provider: Reference | None = None


class DiagnosticReportView(ResourceView):
    status: str | None = None
    code: CodeableConcept = CodeableConcept()
    effective_date_time: str | None = None
    result: list[Reference] = []
    presented_form: list[dict[str, object]] = []

    @property
    def is_note(self) -> bool:
        """Synthea's note reports duplicate a DocumentReference (design.md D3)."""
        return bool(self.presented_form)


class DocumentReferenceView(ResourceView):
    status: str | None = None
    type: CodeableConcept = CodeableConcept()
    date: str | None = None


class CarePlanActivityDetail(FhirModel):
    code: CodeableConcept = CodeableConcept()
    status: str | None = None


class CarePlanActivity(FhirModel):
    detail: CarePlanActivityDetail | None = None


class CarePlanView(ResourceView):
    status: str | None = None
    category: list[CodeableConcept] = []
    period: Period = Period()
    activity: list[CarePlanActivity] = []
    addresses: list[Reference] = []

    @property
    def title(self) -> str:
        # US Core adds a generic "assess-plan" category with no text; the
        # category that has text names the plan.
        named = [c.text for c in self.category if c.text]
        return named[0] if named else ""


class DeviceName(FhirModel):
    name: str | None = None


class DeviceView(ResourceView):
    status: str | None = None
    type: CodeableConcept = CodeableConcept()
    manufacture_date: str | None = None
    device_name: list[DeviceName] = []


class ImagingStudyView(ResourceView):
    status: str | None = None
    started: str | None = None
    procedure_code: list[CodeableConcept] = []


VIEW_TYPES: dict[str, type[ResourceView]] = {
    "Patient": PatientView,
    "Condition": ConditionView,
    "Observation": ObservationView,
    "MedicationRequest": MedicationRequestView,
    "AllergyIntolerance": AllergyIntoleranceView,
    "Immunization": ImmunizationView,
    "Procedure": ProcedureView,
    "Encounter": EncounterView,
    "DiagnosticReport": DiagnosticReportView,
    "DocumentReference": DocumentReferenceView,
    "CarePlan": CarePlanView,
    "Device": DeviceView,
    "ImagingStudy": ImagingStudyView,
}
"""The index allowlist (design.md D3). Billing, Provenance, Medication,
MedicationAdministration, SupplyDelivery and CareTeam are left out; see
docs/data.md for their share of the bundles."""


def parse_view(resource: Resource) -> ResourceView | None:
    """Parse a resource into its view, or None if its type isn't indexed."""
    view_type = VIEW_TYPES.get(resource.get("resourceType", ""))
    return view_type.model_validate(resource) if view_type else None
