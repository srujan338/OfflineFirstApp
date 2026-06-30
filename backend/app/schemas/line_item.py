from pydantic import BaseModel


class LineItem(BaseModel):
    description: str
    quantity: float
    price: float
    total: float
