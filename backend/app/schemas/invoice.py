from pydantic import BaseModel, Field

from app.schemas.line_item import LineItem


class InvoiceData(BaseModel):
    vendor: str
    invoice_number: str
    date: str
    subtotal: float
    tax: float
    total: float
    currency: str = "USD"
    category: str
    line_items: list[LineItem] = Field(default_factory=list)


class StoredInvoice(InvoiceData):
    id: int
    image_path: str | None = None
    created_at: str | None = None
