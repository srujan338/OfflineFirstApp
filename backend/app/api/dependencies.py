from collections.abc import Generator
from sqlite3 import Connection

from app.db.database import get_connection


def get_db() -> Generator[Connection, None, None]:
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()
