import argparse
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

REQUIRED_TABLES = {"invoices", "line_items", "runs"}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Initialize and validate SQLite schema."
    )
    parser.add_argument("--database", help="Optional SQLite path for this run.")
    parser.add_argument(
        "--check", action="store_true", help="Validate required tables."
    )
    args = parser.parse_args()

    if args.database:
        os.environ["DATABASE_URL"] = f"sqlite:///{args.database}"

    from app.db.database import get_connection, init_db

    init_db()

    if args.check:
        conn = get_connection()
        tables = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            )
        }
        conn.close()
        missing = REQUIRED_TABLES - tables
        if missing:
            raise RuntimeError(f"Missing SQLite tables: {sorted(missing)}")

    print("SQLite schema initialized.")


if __name__ == "__main__":
    main()
