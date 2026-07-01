import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.core.errors import ProcessingError, processing_error_handler
from app.core.logging import setup_logging
from app.core.middleware import request_timing_middleware

from app.api.router import api_router
from app.db.database import init_db

logger = setup_logging()
init_db()

app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0")

# CORS — same origin in production, allow * for direct API testing
origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(request_timing_middleware)
app.add_exception_handler(ProcessingError, processing_error_handler)

# API routes
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Invoice Intelligence API running on CPU"}


# ----------------------------------------------------------
# Serve the built React frontend (PWA) from frontend/dist
# ----------------------------------------------------------
FRONTEND_DIST = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist"

if FRONTEND_DIST.exists():
    # Vite emits hashed bundles into /assets — mount as static
    assets_dir = FRONTEND_DIST / "assets"
    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

    # Root-level PWA / favicon files
    @app.get("/manifest.webmanifest", include_in_schema=False)
    @app.get("/sw.js", include_in_schema=False)
    @app.get("/favicon.svg", include_in_schema=False)
    @app.get("/favicon.ico", include_in_schema=False)
    @app.get("/icon-192.png", include_in_schema=False)
    @app.get("/icon-512.png", include_in_schema=False)
    @app.get("/maskable-icon-512.png", include_in_schema=False)
    @app.get("/apple-touch-icon.png", include_in_schema=False)
    def pwa_static(path: str):
        return FileResponse(FRONTEND_DIST / path)

    # SPA fallback — any non-API route serves index.html so React Router works
    @app.get("/{full_path:path}", include_in_schema=False)
    def spa_fallback(full_path: str):
        if full_path.startswith("api/"):
            return JSONResponse({"detail": "Not Found"}, status_code=404)
        index = FRONTEND_DIST / "index.html"
        if index.exists():
            return FileResponse(index)
        return JSONResponse({"detail": "Frontend not built"}, status_code=500)
else:
    @app.get("/")
    def no_frontend():
        return {"status": "ok", "message": "API running. Frontend not built."}
