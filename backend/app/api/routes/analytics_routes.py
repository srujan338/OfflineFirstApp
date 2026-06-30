from fastapi import APIRouter
from app.db.repository import get_all_invoices

router = APIRouter()


# -------------------------
# EXPENDITURE ANALYTICS
# -------------------------
@router.get("/expenditure")
def get_expenditure():
    invoices = get_all_invoices(limit=1000)

    summary = {}

    for inv in invoices:
        cat = inv.get("category") or "other"
        summary[cat] = summary.get(cat, 0) + (inv["total"] or 0)

    return {"success": True, "data": summary}
