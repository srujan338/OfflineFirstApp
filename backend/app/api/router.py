from fastapi import APIRouter

from app.api.routes.invoice_routes import router as invoice_router
from app.api.routes.analytics_routes import router as analytics_router
from app.api.routes.run_routes import router as run_router

api_router = APIRouter()

api_router.include_router(invoice_router, prefix="/invoices", tags=["Invoices"])
api_router.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(run_router, prefix="/runs", tags=["Runs"])
