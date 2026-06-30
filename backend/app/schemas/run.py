from pydantic import BaseModel


class RunMetrics(BaseModel):
    ocr_time: float
    parse_time: float
    total_time: float
    memory: float


class StoredRun(BaseModel):
    id: int
    invoice_id: int | None = None
    ocr_time: float
    parse_time: float
    total_time: float
    memory_usage: float
    created_at: str | None = None
