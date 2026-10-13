"""Shared text utility helpers."""

import re
from collections import Counter


def slugify(text: str) -> str:
    """Lowercase text, join runs of non-ASCII-alphanumerics, and trim hyphens."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def parse_duration(text: str) -> int:
    """Return seconds for compact positive integer components in h, m, s order.

    Each unit may appear once and may be omitted. Raise ValueError for empty
    input or input that does not entirely match this format.
    """
    match = re.fullmatch(
        r"(?:([1-9][0-9]*)h)?(?:([1-9][0-9]*)m)?(?:([1-9][0-9]*)s)?", text
    )
    if match is None or not text:
        raise ValueError(
            "Invalid duration: expected positive integer components using h, m, s "
            "once each in that order, such as '1h30m15s'."
        )

    hours, minutes, seconds = (int(value or "0") for value in match.groups())
    return hours * 3600 + minutes * 60 + seconds


def word_count(text: str) -> dict[str, int]:
    """Count lowercase ASCII words, preserving internal straight apostrophes.

    Other characters separate words. Empty text returns an empty dictionary.
    """
    words = re.findall(r"[a-z]+(?:'[a-z]+)*", text.lower())
    return dict(Counter(words))
