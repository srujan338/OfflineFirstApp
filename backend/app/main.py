from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.errors import ProcessingError, processing_error_handler
from app.core.logging import setup_logging
from app.core.middleware import request_timing_middleware

from app.api.router import api_router
from app.db.database import init_db

logger = setup_logging()

# Auto-initialize SQLite database schema on startup
init_db()

app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0")

# CORS (frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request timing
app.middleware("http")(request_timing_middleware)

# Exception handler
app.add_exception_handler(ProcessingError, processing_error_handler)

# API routes
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Invoice Intelligence API running on CPU"}
