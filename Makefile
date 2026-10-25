.PHONY: setup data profile ingest questions serve eval-retrieval eval-answers eval-selftest fmt lint typecheck test check

SPLIT ?= dev
RUN ?= $(SPLIT)-$(shell date +%Y%m%d)

# Create .venv from uv.lock exactly; fails if the lock is out of date.
setup:
	uv sync --locked

# Regenerate data/cohort/ from a pinned Synthea release. Needs Java 17+.
data:
	bash data/synthea/generate.sh

# Write the cohort profile to docs/data.md.
profile:
	uv run python -m fhir_rag.tools.profile data/cohort > docs/data.md

# Build data/index.sqlite: resources, cards, pinned summaries, embeddings.
ingest:
	uv run python -m fhir_rag.ingest

# Rebuild evals/questions/questions.jsonl from the templates and drafted questions.
questions:
	uv run python -m fhir_rag.evals.build_questions

serve:
	uv run uvicorn --factory fhir_rag.api.main:create_app --port 8000

# Deterministic and free; CI runs it with --check on every pull request.
eval-retrieval:
	uv run python -m fhir_rag.evals.run_retrieval --split $(SPLIT)

# Calls the API (generator and judge). Costs money; see --spend-cap.
eval-answers:
	uv run python -m fhir_rag.evals.run_answers --run $(RUN) --split $(SPLIT)

# Oracle and null runs through the whole harness, offline. Oracle should score
# near the top and null near zero; anything else means the harness is broken.
eval-selftest:
	uv run python -m fhir_rag.evals.run_answers --run selftest-oracle --mode oracle --no-judge
	uv run python -m fhir_rag.evals.run_answers --run selftest-null --mode null --no-judge

# Rewrite files: format, then apply safe lint fixes.
fmt:
	uv run ruff format .
	uv run ruff check --fix .

# Read-only checks, the same ones CI runs.
lint:
	uv run ruff format --check .
	uv run ruff check .

typecheck:
	uv run mypy

test:
	uv run pytest

check: lint typecheck test
