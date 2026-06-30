from pydantic import BaseModel


class ExpenditureResponse(BaseModel):
    success: bool
    data: dict[str, float]
