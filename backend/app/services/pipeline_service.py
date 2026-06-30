import time

from app.services.ocr_service import run_ocr
from app.services.parser_service import parse_invoice_text
from app.services.category_service import categorize_vendor

from app.db.repository import create_invoice, log_run
from app.services.metrics_service import get_memory_usage_mb


def process_invoice(image_path: str):
    start = time.time()

    # OCR
    ocr_start = time.time()
    raw_text = run_ocr(image_path)
    ocr_time = time.time() - ocr_start

    # Parsing
    parse_start = time.time()
    parsed = parse_invoice_text(raw_text)
    parse_time = time.time() - parse_start

    # Category
    parsed["category"] = categorize_vendor(parsed["vendor"])

    # Save
    invoice_id = create_invoice(parsed, image_path)

    total_time = time.time() - start
    memory = get_memory_usage_mb()

    # Log run
    log_run(invoice_id, ocr_time, parse_time, total_time, memory)

    return {
        "success": True,
        "invoice_id": invoice_id,
        "data": parsed,
        "metrics": {
            "ocr_time": round(ocr_time, 3),
            "parse_time": round(parse_time, 3),
            "total_time": round(total_time, 3),
            "memory": memory,
        },
    }
