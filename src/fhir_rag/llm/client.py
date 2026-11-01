"""Claude behind a small interface (PLAN.md D9), so tests and evals can swap in fakes.

AnthropicLLM uses structured outputs (`messages.parse` with a Pydantic
schema) and the API's server-side refusal fallback (`fallbacks="default"`):
if a safety classifier declines a request, the API reruns it on a fallback
model within the same call. The model that actually served the request is
recorded on every result, so evals can see when that happened.

ClaudeCodeLLM runs the same calls through the Claude Code CLI on a Claude
subscription, so evals can run without API credits. `make_llm` picks one from
the settings.

Failures map to a few error types that the API and the eval runner handle
differently: unavailable (retry later), timeout, refusal, bad output.
"""

import asyncio
import json
import os
import tempfile
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

import anthropic
from pydantic import BaseModel, ValidationError

from fhir_rag.config import Effort, Settings

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


# Kept out of the CLI's environment, so it can only use the subscription login:
# the API credentials, and bare mode, which would make it use them.
_NOT_FOR_CLI = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_SIMPLE")


class ClaudeCodeLLM:
    """Claude through the Claude Code CLI (`claude -p`), billed to a Claude subscription.

    Each call runs the CLI with our system prompt in place of Claude Code's,
    no tools, no settings files (so no hooks, plugins or CLAUDE.md), no MCP
    servers, prompt caching off (so token counts match the API path), and
    structured output checked against the schema by --json-schema. The API
    credentials are removed from its environment, so a call can't fall back to
    billing API credits. `config_dir` picks the login (CLAUDE_CONFIG_DIR).

    It isn't the API path byte for byte. Claude Code still puts a line of its
    own in front of the system prompt and adds an environment block with
    today's date and an account reminder, and structured output goes through
    a tool call, which adds a model turn: about 1,000 extra input tokens per
    call in all, and slower calls. The latency recorded is the CLI's time in
    API calls, without process start-up. There is no refusal fallback, and
    Claude Code retries rate limits and server errors itself.
    """

    def __init__(self, binary: str, config_dir: Path | None, timeout_s: float) -> None:
        self._binary = binary
        self._config_dir = config_dir
        self._timeout_s = timeout_s
        # An empty working directory, so no project CLAUDE.md is picked up.
        self._cwd = tempfile.TemporaryDirectory(prefix="fhir-rag-claude-")

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
        args = [
            self._binary,
            "-p",
            "--model", model,
            "--effort", effort,
            "--system-prompt", system,
            "--json-schema", json.dumps(schema.model_json_schema()),
            "--tools", "",
            "--setting-sources", "",
            "--strict-mcp-config",
            "--no-session-persistence",
            "--output-format", "json",
        ]  # fmt: skip
        env = {k: v for k, v in os.environ.items() if k not in _NOT_FOR_CLI}
        env |= {"DISABLE_PROMPT_CACHING": "1", "CLAUDE_CODE_MAX_OUTPUT_TOKENS": str(max_tokens)}
        if self._config_dir is not None:
            env["CLAUDE_CONFIG_DIR"] = str(self._config_dir.expanduser())
        started = time.monotonic()
        try:
            proc = await asyncio.create_subprocess_exec(
                *args,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env,
                cwd=self._cwd.name,
            )
        except FileNotFoundError as e:
            raise LLMUnavailable(f"Claude Code CLI not found: {self._binary}") from e
        try:
            out, err = await asyncio.wait_for(proc.communicate(user.encode()), self._timeout_s)
        except TimeoutError as e:
            raise LLMTimeout(f"claude -p took over {self._timeout_s:.0f}s") from e
        finally:
            if proc.returncode is None:  # timed out or cancelled
                proc.kill()
                await proc.wait()
        wall_s = time.monotonic() - started

        try:
            reply = json.loads(out)
        except json.JSONDecodeError as e:
            detail = (err or out).decode(errors="replace").strip()[:300]
            raise LLMError(f"claude -p exited {proc.returncode}: {detail}") from e
        message = str(reply.get("result") or reply.get("subtype"))[:300]
        if reply.get("stop_reason") == "refusal":
            raise LLMRefused(message)
        if reply.get("is_error"):
            if reply.get("terminal_reason") == "api_error":
                raise LLMUnavailable(f"claude -p: {message}")  # login, usage limit, outage
            raise LLMError(f"claude -p: {message}")
        if reply.get("stop_reason") == "max_tokens":
            raise LLMBadOutput("response hit max_tokens")
        if reply.get("structured_output") is None:
            raise LLMBadOutput("no structured output in the response")
        try:
            parsed = schema.model_validate(reply["structured_output"])
        except ValidationError as e:
            raise LLMBadOutput(f"output didn't match the schema: {e}") from e

        # The model that answered: the requested one, unless the CLI used another.
        used = reply.get("modelUsage") or {}
        served = model
        if used and model not in used:
            served = max(used, key=lambda m: used[m].get("outputTokens", 0))
        u = reply.get("usage") or {}
        api_ms = reply.get("duration_api_ms") or 0
        return LLMResult(
            parsed=parsed,
            model=served,
            usage=Usage(
                input_tokens=u.get("input_tokens", 0),
                output_tokens=u.get("output_tokens", 0),
                cache_read_input_tokens=u.get("cache_read_input_tokens", 0),
                cache_creation_input_tokens=u.get("cache_creation_input_tokens", 0),
            ),
            stop_reason=reply.get("stop_reason"),
            latency_s=api_ms / 1000 if api_ms else wall_s,
            request_id=reply.get("session_id"),
        )


def make_llm(settings: Settings) -> LLMClient | None:
    """The configured backend, or None for the API backend without a key."""
    if settings.llm_backend == "cli":
        return ClaudeCodeLLM(
            settings.claude_cli, settings.claude_config_dir, settings.llm_timeout_s
        )
    if settings.anthropic_api_key is None:
        return None
    return AnthropicLLM(
        settings.anthropic_api_key.get_secret_value(),
        settings.llm_timeout_s,
        settings.llm_max_retries,
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
