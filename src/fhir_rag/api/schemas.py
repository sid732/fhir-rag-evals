"""Request and response models. They define the OpenAPI docs at /docs."""

from typing import Any, Literal

from pydantic import BaseModel, Field


class Health(BaseModel):
    status: Literal["ok"]
    patients: int
    cohort: str
    llm_configured: bool


class Patient(BaseModel):
    id: str
    name: str
    gender: str | None
    birth_date: str | None


class Card(BaseModel):
    id: str = Field(description='card id: the FHIR reference, plus "#n" for note chunks')
    resource_type: str
    date: str | None
    text: str


class PatientDetail(Patient):
    summary: list[Card] = Field(description="the pinned summary every answer gets")


class ResourceOut(BaseModel):
    ref: str
    patient_id: str
    cards: list[Card]
    resource: dict[str, Any] = Field(description="the FHIR R4 resource as stored")


class AskRequest(BaseModel):
    question: str = Field(
        min_length=3, max_length=1000, examples=["What was the most recent HbA1c?"]
    )


class Citation(BaseModel):
    id: str
    resource_ref: str
    url: str


class Sentence(BaseModel):
    text: str
    citations: list[Citation]
    invalid_citations: list[str] = Field(
        description="ids the model cited that weren't in its context; removed from citations"
    )


class RetrievedCard(BaseModel):
    id: str
    rank: int
    source: Literal["summary", "ranked", "series"]
    score: float


class Latency(BaseModel):
    retrieval_ms: float
    llm_ms: float
    total_ms: float


class TokenUsage(BaseModel):
    input_tokens: int
    output_tokens: int


class AskResponse(BaseModel):
    request_id: str
    status: Literal["answered", "not_in_record"]
    answer: str
    sentences: list[Sentence]
    retrieved: list[RetrievedCard]
    model: str
    usage: TokenUsage
    cost_usd: float | None
    latency: Latency
    prompt_version: str


class ErrorOut(BaseModel):
    detail: str
    request_id: str | None = None
