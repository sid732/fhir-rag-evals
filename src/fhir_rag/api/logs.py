"""JSON logs with a request id on every line (PLAN.md D17).

Logs carry ids, counts, timings and token usage. They never carry question
text or record text: with real PHI, the same rule keeps the logs out of
scope, and an access audit trail would go to a separate, controlled store.
"""

import json
import logging
from contextvars import ContextVar

request_id_var: ContextVar[str | None] = ContextVar("request_id", default=None)


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        entry: dict[str, object] = {
            "level": record.levelname.lower(),
            "logger": record.name,
            "event": record.getMessage(),
            "request_id": request_id_var.get(),
        }
        fields = getattr(record, "fields", None)
        if isinstance(fields, dict):
            entry.update(fields)
        if record.exc_info:
            entry["error"] = self.formatException(record.exc_info)
        return json.dumps(entry, default=str)


def configure(level: int = logging.INFO) -> None:
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    root = logging.getLogger("fhir_rag")
    root.handlers = [handler]
    root.setLevel(level)
    root.propagate = False
