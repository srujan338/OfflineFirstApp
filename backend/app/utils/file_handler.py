from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.core.config import settings

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".pdf"}


def validate_file_type(filename: str) -> str:
    suffix = Path(filename or "").suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        allowed = ", ".join(sorted(ALLOWED_EXTENSIONS))
        raise ValueError(f"Unsupported file type. Allowed types: {allowed}")
    return suffix


def generate_unique_filename(original_filename: str) -> str:
    suffix = validate_file_type(original_filename)
    return f"{uuid4().hex}{suffix}"


async def save_upload_file(upload_file: UploadFile, upload_dir: str | Path) -> Path:
    upload_path = Path(upload_dir)
    upload_path.mkdir(parents=True, exist_ok=True)

    filename = generate_unique_filename(upload_file.filename or "")
    destination = upload_path / filename

    contents = await upload_file.read()
    max_bytes = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    if len(contents) > max_bytes:
        raise ValueError(f"File exceeds {settings.MAX_UPLOAD_SIZE_MB} MB limit")

    destination.write_bytes(contents)
    return destination
