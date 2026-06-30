from fastapi import APIRouter, File, HTTPException, Query, UploadFile

from app.core.config import settings
from app.db.repository import (
    get_all_invoices,
    get_invoice_by_id,
    update_invoice_category,
)
from app.services.category_service import update_category as remember_category
from app.services.pipeline_service import process_invoice
from app.utils.file_handler import save_upload_file

router = APIRouter()


# -------------------------
# UPLOAD + PROCESS INVOICE
# -------------------------
@router.post("/process")
async def process(file: UploadFile = File(...)):
    try:
        file_path = await save_upload_file(file, settings.UPLOAD_DIR)
        return process_invoice(str(file_path))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------
# GET ALL INVOICES
# -------------------------
@router.get("/")
def list_invoices(limit: int = Query(50), offset: int = Query(0)):
    return {"success": True, "data": get_all_invoices(limit, offset)}


# -------------------------
# GET SINGLE INVOICE
# -------------------------
@router.get("/{invoice_id}")
def get_invoice(invoice_id: int):
    invoice = get_invoice_by_id(invoice_id)

    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    return {"success": True, "data": invoice}


# -------------------------
# UPDATE CATEGORY (USER CORRECTION TO LEARNING)
# -------------------------
@router.put("/{invoice_id}/category")
def update_category(invoice_id: int, category: str):
    invoice = get_invoice_by_id(invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    update_invoice_category(invoice_id, category)
    remember_category(invoice["vendor"], category)

    return {"success": True, "message": "Category updated successfully"}
