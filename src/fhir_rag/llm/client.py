"""Claude behind a small interface (PLAN.md D9), so tests and evals can swap in fakes.

AnthropicLLM uses structured outputs (`messages.parse` with a Pydantic
schema) and the API's server-side refusal fallback (`fallbacks="default"`):
if a safety classifier declines a request, the API reruns it on a fallback
model within the same call. The model that actually served the request is
recorded on every result, so evals can see when that happened.

Failures map to a few error types that the API and the eval runner handle
differently: unavailable (retry later), timeout, refusal, bad output.
"""

import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any, Protocol

import anthropic
from pydantic import BaseModel, ValidationError

from fhir_rag.config import Effort

FALLBACK_BETA = "server-side-fallback-2026-07-01"


@dataclass(frozen=True)
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_input_tokens: int = 0
    cache_creation_input_tokens: int = 0


@dataclass(frozen=True)
class LLMResult[T: BaseModel]:
    parsed: T
    model: str  # the model that served the request, from the response
    usage: Usage
    stop_reason: str | None
    latency_s: float
    request_id: str | None = None


class LLMError(Exception):
    kind = "error"


class LLMUnavailable(LLMError):
    kind = "unavailable"  # missing credentials, rate limits, 5xx after retries


class LLMTimeout(LLMError):
    kind = "timeout"


class LLMRefused(LLMError):
    kind = "refusal"


class LLMBadOutput(LLMError):
    kind = "bad_output"  # truncated at max_tokens, or didn't match the schema


class LLMClient(Protocol):
    async def parse[T: BaseModel](
        self,
        *,
        model: str,
        system: str,
        user: str,
        schema: type[T],
        effort: Effort,
        max_tokens: int,
    ) -> LLMResult[T]: ...


class AnthropicLLM:
    def __init__(self, api_key: str | None, timeout_s: float, max_retries: int) -> None:
        self._client = anthropic.AsyncAnthropic(
            api_key=api_key, timeout=timeout_s, max_retries=max_retries
        )

    async def parse[T: BaseModel](
        self,
        *,
        model: str,
        system: str,
        user: str,
        schema: type[T],
        effort: Effort,
        max_tokens: int,
    ) -> LLMResult[T]:
        started = time.monotonic()
        try:
            response = await self._client.beta.messages.parse(
                model=model,
                max_tokens=max_tokens,
                system=system,
                messages=[{"role": "user", "content": user}],
                output_format=schema,
                output_config={"effort": effort},
                betas=[FALLBACK_BETA],
                fallbacks="default",
            )
        except anthropic.APITimeoutError as e:
            raise LLMTimeout(str(e)) from e
        except (anthropic.AuthenticationError, anthropic.PermissionDeniedError) as e:
            raise LLMUnavailable(f"credentials rejected: {e.message}") from e
        except anthropic.RateLimitError as e:
            raise LLMUnavailable(f"rate limited: {e.message}") from e
        except anthropic.APIStatusError as e:
            if e.status_code >= 500:
                raise LLMUnavailable(f"server error {e.status_code}") from e
            raise LLMError(f"request rejected ({e.status_code}): {e.message}") from e
        except anthropic.APIConnectionError as e:
            raise LLMUnavailable(f"connection failed: {e}") from e
        except ValidationError as e:
            raise LLMBadOutput(f"output didn't match the schema: {e}") from e

        if response.stop_reason == "refusal":
            raise LLMRefused(str(response.stop_details))
        if response.stop_reason == "max_tokens":
            raise LLMBadOutput("response hit max_tokens")
        parsed = response.parsed_output
        if parsed is None:
            raise LLMBadOutput("no structured output in the response")
        u = response.usage
        return LLMResult(
            parsed=parsed,
            model=response.model,
            usage=Usage(
                input_tokens=u.input_tokens,
                output_tokens=u.output_tokens,
                cache_read_input_tokens=u.cache_read_input_tokens or 0,
                cache_creation_input_tokens=u.cache_creation_input_tokens or 0,
            ),
            stop_reason=response.stop_reason,
            latency_s=time.monotonic() - started,
            request_id=getattr(response, "_request_id", None),
        )


type Responder = Callable[[str, str, type[Any]], Awaitable[Any] | Any]


class FakeLLM:
    """Returns whatever `respond(system, user, schema)` builds. For tests and offline runs."""

    def __init__(self, respond: Responder, model: str = "fake-model") -> None:
        self._respond = respond
        self._model = model
        self.calls: list[tuple[str, str]] = []

    async def parse[T: BaseModel](
        self,
        *,
        model: str,
        system: str,
        user: str,
        schema: type[T],
        effort: Effort,
        max_tokens: int,
    ) -> LLMResult[T]:
        self.calls.append((system, user))
        value = self._respond(system, user, schema)
        if isinstance(value, Awaitable):
            value = await value
        if isinstance(value, LLMError):
            raise value
        parsed = schema.model_validate(value)
        usage = Usage(input_tokens=len(user) // 4, output_tokens=50)
        return LLMResult(parsed, self._model, usage, "end_turn", 0.0)
