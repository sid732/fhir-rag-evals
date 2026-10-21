# fhir-rag-evals

A FastAPI service that answers questions about one synthetic patient's FHIR R4 record and cites the resources behind each sentence, plus an evaluation harness that measures retrieval and answer quality. Work in progress; see [docs/PLAN.md](docs/PLAN.md).

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
make setup   # create .venv from uv.lock
make check   # lint, type check, tests
```
