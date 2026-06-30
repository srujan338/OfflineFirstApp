from typing import Optional

from pydantic import BaseModel, Field


class LineItem(BaseModel):
    description: str
    quantity: float
    price: float
    total: float


class Invoice(BaseModel):
    id: Optional[int] = None
    vendor: str
    invoice_number: str
    date: str
    subtotal: float
    tax: float
    total: float
    currency: str = "USD"
    category: str
    image_path: Optional[str] = None
    line_items: list[LineItem] = Field(default_factory=list)
