import re
import string

PRINTABLE = set(string.printable)


def remove_garbage_characters(text: str) -> str:
    if not text:
        return ""
    return "".join(ch for ch in text if ch in PRINTABLE)


def normalize_whitespace(text: str) -> str:
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines()]
    compact_lines = [line for line in lines if line]
    return "\n".join(compact_lines)


def clean_ocr_text(text: str) -> str:
    cleaned = remove_garbage_characters(text)
    cleaned = cleaned.replace("\r\n", "\n").replace("\r", "\n")
    return normalize_whitespace(cleaned)
