"""ClaudeCodeLLM against a fake `claude` executable that records how it was called."""

import asyncio
import json
import sys
import time
from pathlib import Path
from typing import Any

import pytest
from pydantic import BaseModel

from fhir_rag.config import Settings
from fhir_rag.llm.client import (
    AnthropicLLM,
    ClaudeCodeLLM,
    LLMBadOutput,
    LLMError,
    LLMRefused,
    LLMResult,
    LLMTimeout,
    LLMUnavailable,
    make_llm,
)

FAKE_CLAUDE = """\
import json, os, sys, time
log = {"argv": sys.argv[1:], "stdin": sys.stdin.read(), "cwd": os.getcwd(), "env": dict(os.environ)}
with open(os.environ["FAKE_CLAUDE_LOG"], "w") as f:
    json.dump(log, f)
time.sleep(float(os.environ.get("FAKE_CLAUDE_SLEEP", "0")))
print(os.environ["FAKE_CLAUDE_REPLY"])
"""

OK_REPLY = {
    "type": "result",
    "is_error": False,
    "stop_reason": "end_turn",
    "terminal_reason": "completed",
    "result": '{"answer": "Four"}',
    "structured_output": {"answer": "Four"},
    "duration_ms": 1800,
    "duration_api_ms": 1500,
    "session_id": "abc",
    "usage": {"input_tokens": 1323, "output_tokens": 53},
    "modelUsage": {"claude-sonnet-5-5": {"inputTokens": 1323, "outputTokens": 53}},
}


class Out(BaseModel):
    answer: str


@pytest.fixture
def fake_claude(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    script = tmp_path / "claude"
    script.write_text(f"#!{sys.executable}\n{FAKE_CLAUDE}")
    script.chmod(0o755)
    monkeypatch.setenv("FAKE_CLAUDE_LOG", str(tmp_path / "call.json"))
    monkeypatch.setenv("FAKE_CLAUDE_REPLY", json.dumps(OK_REPLY))
    return script


def _call(llm: ClaudeCodeLLM) -> LLMResult[Out]:
    return asyncio.run(
        llm.parse(
            model="claude-sonnet-5-5",
            system="You answer questions.",
            user="What is 2+2?",
            schema=Out,
            effort="low",
            max_tokens=123,
        )
    )


def test_cli_call_runs_isolated_and_never_sees_the_api_key(
    fake_claude: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test")
    llm = ClaudeCodeLLM(str(fake_claude), tmp_path / "login", 10)
    result = _call(llm)
    assert result.parsed == Out(answer="Four")
    assert result.model == "claude-sonnet-5-5"
    assert (result.usage.input_tokens, result.usage.output_tokens) == (1323, 53)
    assert result.latency_s == 1.5  # the CLI's API time, not process start-up
    assert result.request_id == "abc"

    call = json.loads((tmp_path / "call.json").read_text())
    argv = call["argv"]
    assert call["stdin"] == "What is 2+2?"
    assert argv[argv.index("--system-prompt") + 1] == "You answer questions."
    assert json.loads(argv[argv.index("--json-schema") + 1]) == Out.model_json_schema()
    assert argv[argv.index("--tools") + 1] == ""
    assert argv[argv.index("--setting-sources") + 1] == ""
    assert {"--strict-mcp-config", "--no-session-persistence"} <= set(argv)
    env = call["env"]
    assert "ANTHROPIC_API_KEY" not in env
    assert env["CLAUDE_CONFIG_DIR"] == str(tmp_path / "login")
    assert env["DISABLE_PROMPT_CACHING"] == "1"
    assert env["CLAUDE_CODE_MAX_OUTPUT_TOKENS"] == "123"
    assert list(Path(call["cwd"]).iterdir()) == []  # no project CLAUDE.md to pick up


def test_cli_records_the_model_that_actually_answered(
    fake_claude: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    usage = {"claude-opus-4-8": {"outputTokens": 50}, "claude-haiku-5-5": {"outputTokens": 3}}
    monkeypatch.setenv("FAKE_CLAUDE_REPLY", json.dumps(OK_REPLY | {"modelUsage": usage}))
    assert _call(ClaudeCodeLLM(str(fake_claude), None, 10)).model == "claude-opus-4-8"


@pytest.mark.parametrize(
    ("reply", "error"),
    [
        (
            OK_REPLY
            | {"is_error": True, "terminal_reason": "api_error", "result": "OAuth expired"},
            LLMUnavailable,
        ),
        (OK_REPLY | {"stop_reason": "refusal"}, LLMRefused),
        (OK_REPLY | {"stop_reason": "max_tokens"}, LLMBadOutput),
        (OK_REPLY | {"structured_output": None}, LLMBadOutput),
        (OK_REPLY | {"structured_output": {"wrong": 1}}, LLMBadOutput),
        (OK_REPLY | {"is_error": True, "terminal_reason": "max_turns"}, LLMError),
        ("not json", LLMError),
    ],
)
def test_cli_failures_map_to_llm_errors(
    fake_claude: Path, monkeypatch: pytest.MonkeyPatch, reply: Any, error: type[LLMError]
) -> None:
    monkeypatch.setenv("FAKE_CLAUDE_REPLY", reply if isinstance(reply, str) else json.dumps(reply))
    with pytest.raises(LLMError) as raised:
        _call(ClaudeCodeLLM(str(fake_claude), None, 10))
    assert type(raised.value) is error


def test_cli_timeout_kills_the_process(fake_claude: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FAKE_CLAUDE_SLEEP", "30")
    started = time.monotonic()
    with pytest.raises(LLMTimeout):
        _call(ClaudeCodeLLM(str(fake_claude), None, 0.5))
    assert time.monotonic() - started < 10


def test_missing_cli_is_unavailable(tmp_path: Path) -> None:
    with pytest.raises(LLMUnavailable):
        _call(ClaudeCodeLLM(str(tmp_path / "no-such-claude"), None, 10))


def test_make_llm_follows_the_backend_setting(settings: Settings) -> None:
    assert make_llm(settings.model_copy(update={"anthropic_api_key": None})) is None
    keyed = Settings(_env_file=None, ANTHROPIC_API_KEY="sk-ant-test", llm_backend="api")
    assert isinstance(make_llm(keyed), AnthropicLLM)
    cli = settings.model_copy(update={"llm_backend": "cli", "anthropic_api_key": None})
    assert isinstance(make_llm(cli), ClaudeCodeLLM)
