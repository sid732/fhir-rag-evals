"""Settings, read from environment variables (prefix FHIR_RAG_) and .env."""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

type RetrievalMode = Literal["bm25", "dense", "hybrid"]
type Effort = Literal["low", "medium", "high", "xhigh", "max"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="FHIR_RAG_", env_file=".env", extra="ignore", frozen=True
    )

    cohort_dir: Path = Path("data/cohort")
    db_path: Path = Path("data/index.sqlite")
    # The date the synthetic record is current as of: Synthea's -e end date.
    record_as_of: str = "2026-10-01"

    embedding_model: str = "BAAI/bge-small-en-v1.5"
    retrieval_mode: RetrievalMode = "hybrid"
    top_k: int = 10
    # Show the newest N results of any series a retrieved card belongs to.
    series_expansion: int = 3
    # Put the patient summary (active problems and meds, allergies, recent
    # visits and immunizations) in front of every answer's context.
    pin_summary: bool = True

    generator_model: str = "claude-opus-5-5"
    generator_effort: Effort = "medium"
    judge_model: str = "claude-sonnet-5-5"
    judge_effort: Effort = "medium"
    max_output_tokens: int = 8000
    llm_timeout_s: float = 90.0
    llm_max_retries: int = 2

    # Read without the prefix, as the Anthropic SDK does. Never logged.
    anthropic_api_key: SecretStr | None = Field(default=None, validation_alias="ANTHROPIC_API_KEY")

    @field_validator("anthropic_api_key", mode="before")
    @classmethod
    def _blank_key_is_unset(cls, value: object) -> object:
        # .env.example ships "ANTHROPIC_API_KEY=" with no value.
        return None if isinstance(value, str) and not value.strip() else value


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
