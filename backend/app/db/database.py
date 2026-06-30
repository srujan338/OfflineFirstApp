import os
import sqlite3
from pathlib import Path

from app.core.config import settings


def get_database_path() -> str:
    database_url = os.getenv("DATABASE_URL", settings.DATABASE_URL)
    if not database_url.startswith("sqlite:///"):
        raise ValueError("Only SQLite database URLs are supported")
    return database_url.replace("sqlite:///", "", 1)


def get_connection():
    db_path = Path(get_database_path())
    if db_path.parent:
        db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn



def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor TEXT,
        invoice_number TEXT,
        date TEXT,
        subtotal REAL,
        tax REAL,
        total REAL,
        currency TEXT DEFAULT 'USD',
        category TEXT,
        image_path TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS line_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_id INTEGER,
        description TEXT,
        quantity REAL,
        price REAL,
        total REAL,
        FOREIGN KEY(invoice_id) REFERENCES invoices(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_id INTEGER,
        ocr_time REAL,
        parse_time REAL,
        total_time REAL,
        memory_usage REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(invoice_id) REFERENCES invoices(id) ON DELETE SET NULL
    );
    """)

    conn.commit()
    conn.close()
