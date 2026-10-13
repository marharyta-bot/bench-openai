"""Shared text normalization helpers."""

import re


def slugify(text: str) -> str:
    """Lowercase text, join runs of non-ASCII-alphanumerics, and trim hyphens."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
