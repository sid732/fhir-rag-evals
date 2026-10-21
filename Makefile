.PHONY: setup fmt lint typecheck test check

# Create .venv from uv.lock exactly; fails if the lock is out of date.
setup:
	uv sync --locked

# Rewrite files: format, then apply safe lint fixes.
fmt:
	uv run ruff format .
	uv run ruff check --fix .

# Read-only checks, the same ones CI will run.
lint:
	uv run ruff format --check .
	uv run ruff check .

typecheck:
	uv run mypy

test:
	uv run pytest

check: lint typecheck test
