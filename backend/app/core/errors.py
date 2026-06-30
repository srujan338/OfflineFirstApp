from fastapi import Request
from fastapi.responses import JSONResponse


class ProcessingError(Exception):
    def __init__(self, message: str):
        self.message = message


async def processing_error_handler(request: Request, exc: Exception) -> JSONResponse:
    message = exc.message if isinstance(exc, ProcessingError) else str(exc)
    return JSONResponse(status_code=500, content={"success": False, "error": message})
