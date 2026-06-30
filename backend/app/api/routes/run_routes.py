from fastapi import APIRouter
from app.db.database import get_connection

router = APIRouter()


# -------------------------
# PIPELINE PERFORMANCE METRICS
# -------------------------
@router.get("/")
def get_runs():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM runs
            ORDER BY created_at DESC
            LIMIT 50
            """)
        rows = cursor.fetchall()
    finally:
        conn.close()

    return {"success": True, "data": [dict(r) for r in rows]}
