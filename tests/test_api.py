from typing import Any

from cohort import P1, P2
from fastapi.testclient import TestClient

from fhir_rag.api.main import AppState, create_app
from fhir_rag.config import Settings
from fhir_rag.llm.answer import AnswerService
from fhir_rag.llm.client import FakeLLM, LLMTimeout, LLMUnavailable
from fhir_rag.retrieval.retriever import Retriever
from fhir_rag.store import Store


def _client(
    store: Store, retriever: Retriever, settings: Settings, llm: FakeLLM | None
) -> TestClient:
    answers = AnswerService(retriever, llm, settings) if llm else None
    return TestClient(create_app(AppState(settings, store, retriever, answers)))


def _cite_a1c(system: str, user: str, schema: type[Any]) -> dict[str, Any]:
    return {
        "status": "answered",
        "sentences": [
            {
                "text": "The most recent HbA1c was 6.8 % on 2026-03-04.",
                "citations": ["Observation/p1-a1c-2026", "Observation/not-in-context"],
            }
        ],
    }


def test_health_and_patients(store: Store, retriever: Retriever, settings: Settings) -> None:
    with _client(store, retriever, settings, None) as client:
        health = client.get("/health").json()
        assert health["patients"] == 2 and health["llm_configured"] is False
        assert [p["id"] for p in client.get("/patients").json()] == [P1, P2]
        detail = client.get(f"/patients/{P1}").json()
        assert detail["summary"][0]["id"] == "Condition/p1-htn"
        assert client.get("/patients/nobody").status_code == 404


def test_resource_lookup_is_scoped_to_the_patient(
    store: Store, retriever: Retriever, settings: Settings
) -> None:
    with _client(store, retriever, settings, None) as client:
        found = client.get(f"/patients/{P1}/resources/Observation/p1-a1c-2026")
        assert found.status_code == 200
        body = found.json()
        assert body["resource"]["valueQuantity"]["value"] == 6.8
        assert body["cards"][0]["id"] == "Observation/p1-a1c-2026"
        # The same resource asked for under another patient is not found.
        assert client.get(f"/patients/{P2}/resources/Observation/p1-a1c-2026").status_code == 404


def test_ask_returns_checked_citations_with_links(
    store: Store, retriever: Retriever, settings: Settings
) -> None:
    with _client(store, retriever, settings, FakeLLM(_cite_a1c)) as client:
        response = client.post(
            f"/patients/{P1}/ask", json={"question": "What was the most recent hemoglobin A1c?"}
        )
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "answered"
    [sentence] = body["sentences"]
    assert [c["id"] for c in sentence["citations"]] == ["Observation/p1-a1c-2026"]
    assert sentence["citations"][0]["url"] == f"/patients/{P1}/resources/Observation/p1-a1c-2026"
    assert sentence["invalid_citations"] == ["Observation/not-in-context"]
    assert response.headers["x-request-id"] == body["request_id"]
    assert {r["source"] for r in body["retrieved"]} >= {"summary"}


def test_ask_errors(store: Store, retriever: Retriever, settings: Settings) -> None:
    with _client(store, retriever, settings, None) as client:
        assert client.post(f"/patients/{P1}/ask", json={"question": "anything?"}).status_code == 503
        assert client.post(f"/patients/{P1}/ask", json={"question": ""}).status_code == 422
    with _client(store, retriever, settings, FakeLLM(lambda s, u, t: LLMTimeout("slow"))) as client:
        assert client.post(f"/patients/{P1}/ask", json={"question": "anything?"}).status_code == 504
        assert (
            client.post("/patients/nobody/ask", json={"question": "anything?"}).status_code == 404
        )
    with _client(
        store, retriever, settings, FakeLLM(lambda s, u, t: LLMUnavailable("down"))
    ) as client:
        response = client.post(f"/patients/{P1}/ask", json={"question": "anything?"})
        assert response.status_code == 503 and "unavailable" in response.json()["detail"]
