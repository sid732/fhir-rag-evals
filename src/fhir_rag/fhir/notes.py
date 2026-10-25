"""Clinical notes: decode them from DocumentReference and split them into chunks.

Synthea writes one note per encounter as base64 text with markdown-style
section headers ("# Chief Complaint", "# Medications", ...). Notes run 61 to
881 words (docs/data.md); bge-small reads at most 512 tokens, so long notes are
split at section boundaries into chunks of about CHUNK_WORDS words.
"""

import base64
import re

from fhir_rag.fhir.loader import Resource

CHUNK_WORDS = 200
_SECTION = re.compile(r"^(?=#\s)", flags=re.MULTILINE)


def note_text(document_reference: Resource) -> str:
    """Decode the clinical note in a DocumentReference.

    Synthea puts the note in content[0].attachment.data as base64 UTF-8 text.
    Returns "" when there is no inline data.
    """
    content = document_reference.get("content") or [{}]
    data = content[0].get("attachment", {}).get("data")
    if not data:
        return ""
    return base64.b64decode(data).decode("utf-8")


def split_note(text: str, max_words: int = CHUNK_WORDS) -> list[str]:
    """Split a note into chunks of whole sections, each up to max_words words.

    Sections are packed in order. A single section longer than max_words is
    split on word boundaries. Whitespace inside each chunk is normalized.
    """
    sections = [" ".join(s.split()) for s in _SECTION.split(text)]
    chunks: list[str] = []
    current: list[str] = []
    for section in (s for s in sections if s):
        words = section.split()
        while len(words) > max_words:
            if current:
                chunks.append(" ".join(current))
                current = []
            chunks.append(" ".join(words[:max_words]))
            words = words[max_words:]
        if current and len(current) + len(words) > max_words:
            chunks.append(" ".join(current))
            current = []
        current.extend(words)
    if current:
        chunks.append(" ".join(current))
    return chunks
