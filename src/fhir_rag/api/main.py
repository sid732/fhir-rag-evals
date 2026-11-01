"""The FastAPI app.

    uvicorn --factory fhir_rag.api.main:create_app

Dependencies (store, retriever, answer service) live on app.state and are
built in the lifespan, or passed in by tests, which swap the LLM for a fake.
"""

import logging
import time
import uuid
from collections.abc import AsyncIterator, Awaitable, Callable
from contextlib import asynccontextmanager
from dataclasses import dataclass

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse

from fhir_rag.api import logs
from fhir_rag.api.schemas import (
    AskRequest,
    AskResponse,
    Card,
    Citation,
    ErrorOut,
    Health,
    Latency,
    Patient,
    PatientDetail,
    ResourceOut,
    RetrievedCard,
    Sentence,
    TokenUsage,
)
from fhir_rag.config import Settings, get_settings
from fhir_rag.fhir.cards import Chunk
from fhir_rag.llm.answer import AnswerService
from fhir_rag.llm.client import (
    LLMBadOutput,
    LLMError,
    LLMRefused,
    LLMTimeout,
    LLMUnavailable,
    make_llm,
)
from fhir_rag.retrieval.retriever import Retriever, UnknownPatientError
from fhir_rag.store import Store

log = logging.getLogger("fhir_rag.api")


@dataclass
class AppState:
    settings: Settings
    store: Store
    retriever: Retriever
    answers: AnswerService | None  # None for the API backend without a key


def build_state(settings: Settings) -> AppState:
    if not settings.db_path.exists():
        raise RuntimeError(f"{settings.db_path} not found; run `make ingest` first")
    from fhir_rag.retrieval.dense import FastEmbedEmbedder

    store = Store(settings.db_path)
    retriever = Retriever(store, FastEmbedEmbedder(settings.embedding_model))
    llm = make_llm(settings)
    answers = AnswerService(retriever, llm, settings) if llm else None
    return AppState(settings, store, retriever, answers)


def _card(chunk: Chunk) -> Card:
    return Card(
        id=chunk.chunk_id,
        resource_type=chunk.resource_type,
        date=chunk.date,
        text=chunk.text,
    )


def _resource_url(patient_id: str, ref: str) -> str:
    rtype, rid = ref.split("/", 1)
    return f"/patients/{patient_id}/resources/{rtype}/{rid}"


def create_app(state: AppState | None = None) -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        logs.configure()
        app.state.deps = state or build_state(get_settings())
        log.info(
            "started",
            extra={"fields": {"patients": len(app.state.deps.store.patients())}},
        )
        yield
        if state is None:
            app.state.deps.store.close()

    app = FastAPI(
        title="fhir-rag-evals",
        summary="Cited answers about one synthetic patient's FHIR R4 record.",
        version="0.1.0",
        lifespan=lifespan,
        responses={404: {"model": ErrorOut}, 503: {"model": ErrorOut}},
    )

    def deps(request: Request) -> AppState:
        result: AppState = request.app.state.deps
        return result

    @app.middleware("http")
    async def request_id(
        request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        rid = request.headers.get("x-request-id") or uuid.uuid4().hex[:16]
        token = logs.request_id_var.set(rid)
        started = time.monotonic()
        try:
            response = await call_next(request)
        finally:
            logs.request_id_var.reset(token)
        response.headers["x-request-id"] = rid
        log.info(
            "request",
            extra={
                "fields": {
                    "request_id": rid,
                    "method": request.method,
                    "route": request.scope.get("route").path  # type: ignore[union-attr]
                    if request.scope.get("route")
                    else request.url.path,
                    "status": response.status_code,
                    "ms": round(1000 * (time.monotonic() - started), 1),
                }
            },
        )
        return response

    @app.exception_handler(LLMError)
    async def llm_error(request: Request, exc: LLMError) -> JSONResponse:
        status = {
            LLMUnavailable: 503,
            LLMTimeout: 504,
            LLMRefused: 502,
            LLMBadOutput: 502,
        }.get(type(exc), 502)
        log.warning("llm_error", extra={"fields": {"kind": exc.kind, "status": status}})
        return JSONResponse(
            status_code=status,
            content={
                "detail": f"model call failed ({exc.kind})",
                "request_id": logs.request_id_var.get(),
            },
        )

    @app.get("/health")
    def health(request: Request) -> Health:
        d = deps(request)
        return Health(
            status="ok",
            patients=len(d.store.patients()),
            cohort=d.store.meta("cohort_hash") or "",
            llm_configured=d.answers is not None,
        )

    @app.get("/patients")
    def list_patients(request: Request) -> list[Patient]:
        return [
            Patient(id=p.patient_id, name=p.name, gender=p.gender, birth_date=p.birth_date)
            for p in deps(request).store.patients()
        ]

    @app.get("/patients/{patient_id}")
    def get_patient(patient_id: str, request: Request) -> PatientDetail:
        d = deps(request)
        p = d.store.patient(patient_id)
        if p is None:
            raise HTTPException(404, "unknown patient")
        index = d.retriever.index(patient_id)
        return PatientDetail(
            id=p.patient_id,
            name=p.name,
            gender=p.gender,
            birth_date=p.birth_date,
            summary=[_card(index.by_id[ref]) for ref in index.pinned_refs],
        )

    @app.get("/patients/{patient_id}/resources/{resource_type}/{resource_id}")
    def get_resource(
        patient_id: str, resource_type: str, resource_id: str, request: Request
    ) -> ResourceOut:
        d = deps(request)
        ref = f"{resource_type}/{resource_id}"
        found = d.store.resource(ref)
        # A resource from another patient's record is reported as not found,
        # so the endpoint can't confirm that it exists.
        if found is None or found[0] != patient_id:
            raise HTTPException(404, "unknown resource for this patient")
        cards = [c for c in d.retriever.index(patient_id).chunks if c.resource_ref == ref]
        return ResourceOut(
            ref=ref,
            patient_id=patient_id,
            cards=[_card(c) for c in cards],
            resource=found[1],
        )

    @app.post("/patients/{patient_id}/ask")
    async def ask(patient_id: str, body: AskRequest, request: Request) -> AskResponse:
        d = deps(request)
        if d.store.patient(patient_id) is None:
            raise HTTPException(404, "unknown patient")
        if d.answers is None:
            raise HTTPException(503, "no ANTHROPIC_API_KEY configured")
        try:
            result = await d.answers.answer(patient_id, body.question)
        except UnknownPatientError as e:
            raise HTTPException(404, "unknown patient") from e
        by_id = {r.chunk.chunk_id: r.chunk for r in result.retrieved}
        by_ref = {r.chunk.resource_ref: r.chunk for r in result.retrieved}
        sentences = []
        for s in result.answer.sentences:
            citations = []
            for c in s.citations:
                chunk = by_id.get(c) or by_ref[c]
                citations.append(
                    Citation(
                        id=c,
                        resource_ref=chunk.resource_ref,
                        url=_resource_url(patient_id, chunk.resource_ref),
                    )
                )
            sentences.append(
                Sentence(text=s.text, citations=citations, invalid_citations=s.invalid)
            )
        log.info(
            "answered",
            extra={
                "fields": {
                    "patient_id": patient_id,
                    "status": result.answer.status,
                    "cards": len(result.retrieved),
                    "invalid_citations": len(result.answer.invalid_citations),
                    "model": result.model,
                    "input_tokens": result.usage.input_tokens,
                    "output_tokens": result.usage.output_tokens,
                    "llm_ms": round(1000 * result.llm_s, 1),
                }
            },
        )
        return AskResponse(
            request_id=logs.request_id_var.get() or "",
            status=result.answer.status,
            answer=result.answer.text,
            sentences=sentences,
            retrieved=[
                RetrievedCard(id=r.chunk.chunk_id, rank=r.rank, source=r.source, score=r.score)
                for r in result.retrieved
            ],
            model=result.model,
            usage=TokenUsage(
                input_tokens=result.usage.input_tokens,
                output_tokens=result.usage.output_tokens,
            ),
            cost_usd=result.cost_usd,
            latency=Latency(
                retrieval_ms=round(1000 * result.retrieval_s, 1),
                llm_ms=round(1000 * result.llm_s, 1),
                total_ms=round(1000 * result.total_s, 1),
            ),
            prompt_version=result.prompt_version,
        )

    return app
