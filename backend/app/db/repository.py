from typing import Any
from app.db.database import get_connection


def create_invoice(invoice: dict, image_path: str) -> int:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO invoices (
                vendor, invoice_number, date, subtotal, tax,
                total, currency, category, image_path
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                invoice.get("vendor"),
                invoice.get("invoice_number"),
                invoice.get("date"),
                invoice.get("subtotal"),
                invoice.get("tax"),
                invoice.get("total"),
                invoice.get("currency", "USD"),
                invoice.get("category"),
                image_path,
            ),
        )
        invoice_id = cursor.lastrowid

        for item in invoice.get("line_items", []):
            cursor.execute(
                """
                INSERT INTO line_items (
                    invoice_id, description, quantity, price, total
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    invoice_id,
                    item.get("description"),
                    item.get("quantity"),
                    item.get("price"),
                    item.get("total"),
                ),
            )

        conn.commit()
        return int(invoice_id)
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def get_all_invoices(
    limit: int = 50,
    offset: int = 0,
    category: str | None = None,
    search: str | None = None,
) -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM invoices WHERE 1=1"
    params: list[Any] = []

    if category:
        query += " AND category = ?"
        params.append(category)

    if search:
        query += " AND (vendor LIKE ? OR invoice_number LIKE ?)"
        params.append(f"%{search}%")
        params.append(f"%{search}%")

    query += " ORDER BY created_at DESC LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    cursor.execute(query, tuple(params))
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows


def get_invoice_by_id(invoice_id: int) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM invoices WHERE id = ?", (invoice_id,))
    invoice = cursor.fetchone()

    if invoice is None:
        conn.close()
        return None

    cursor.execute("SELECT * FROM line_items WHERE invoice_id = ?", (invoice_id,))
    line_items = [dict(row) for row in cursor.fetchall()]
    data = dict(invoice)
    data["line_items"] = line_items
    conn.close()
    return data


def update_invoice_category(invoice_id: int, category: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE invoices SET category = ? WHERE id = ?",
        (category, invoice_id),
    )
    updated = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return updated


def update_invoice(invoice_id: int, invoice: dict) -> bool:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE invoices SET
                vendor = ?,
                invoice_number = ?,
                date = ?,
                subtotal = ?,
                tax = ?,
                total = ?,
                currency = ?,
                category = ?
            WHERE id = ?
            """,
            (
                invoice.get("vendor"),
                invoice.get("invoice_number"),
                invoice.get("date"),
                invoice.get("subtotal"),
                invoice.get("tax"),
                invoice.get("total"),
                invoice.get("currency", "USD"),
                invoice.get("category"),
                invoice_id,
            ),
        )
        updated = cursor.rowcount > 0

        if "line_items" in invoice:
            cursor.execute("DELETE FROM line_items WHERE invoice_id = ?", (invoice_id,))
            for item in invoice.get("line_items", []):
                cursor.execute(
                    """
                    INSERT INTO line_items (
                        invoice_id, description, quantity, price, total
                    ) VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        invoice_id,
                        item.get("description"),
                        item.get("quantity"),
                        item.get("price"),
                        item.get("total"),
                    ),
                )
        conn.commit()
        return updated
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def log_run(
    invoice_id: int,
    ocr_time: float,
    parse_time: float,
    total_time: float,
    memory_usage: float,
) -> None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO runs (
            invoice_id, ocr_time, parse_time, total_time, memory_usage
        ) VALUES (?, ?, ?, ?, ?)
        """,
        (invoice_id, ocr_time, parse_time, total_time, memory_usage),
    )

    conn.commit()
    conn.close()
