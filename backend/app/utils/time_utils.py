from datetime import UTC, datetime


def utc_timestamp() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def format_duration(seconds: float) -> str:
    if seconds < 0:
        raise ValueError("Duration cannot be negative")
    if seconds < 1:
        return f"{seconds * 1000:.0f}ms"
    if seconds < 60:
        return f"{seconds:.2f}s"

    minutes, remaining_seconds = divmod(seconds, 60)
    return f"{int(minutes)}m {remaining_seconds:.1f}s"
