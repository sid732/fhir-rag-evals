# The API service. The index is built on first start (about 2 to 5 minutes on
# CPU: it downloads the embedding model and embeds every card) and kept in a
# volume, so later starts are fast. See compose.yaml.
FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:0.13.3 /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    FASTEMBED_CACHE_PATH=/app/.cache/fastembed \
    FHIR_RAG_DB_PATH=/app/index/index.sqlite

WORKDIR /app
# Dependencies first, so code changes don't reinstall them.
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --locked --no-dev --no-install-project
COPY src ./src
COPY data/cohort ./data/cohort
RUN uv sync --locked --no-dev

RUN useradd --create-home --uid 1000 app \
    && mkdir -p /app/index /app/.cache \
    && chown -R app /app/index /app/.cache
USER app

EXPOSE 8000
HEALTHCHECK --interval=30s --start-period=10m CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"
CMD ["sh", "-c", "test -f \"$FHIR_RAG_DB_PATH\" || .venv/bin/python -m fhir_rag.ingest; exec .venv/bin/uvicorn --factory fhir_rag.api.main:create_app --host 0.0.0.0 --port 8000"]
