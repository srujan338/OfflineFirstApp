import argparse
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

SAMPLE_INVOICES = [
    {
        "vendor": "ACME Supplies",
        "invoice_number": "INV-1001",
        "date": "2026-06-01",
        "subtotal": 125.00,
        "tax": 12.50,
        "total": 137.50,
        "category": "office",
        "line_items": [
            {
                "description": "Printer paper",
                "quantity": 5,
                "price": 10.00,
                "total": 50.00,
            },
            {
                "description": "Ink cartridge",
                "quantity": 3,
                "price": 25.00,
                "total": 75.00,
            },
        ],
    },
    {
        "vendor": "CloudNet Internet",
        "invoice_number": "CN-2044",
        "date": "2026-06-05",
        "subtotal": 80.00,
        "tax": 8.00,
        "total": 88.00,
        "category": "utilities",
        "line_items": [
            {
                "description": "Business internet",
                "quantity": 1,
                "price": 80.00,
                "total": 80.00,
            },
        ],
    },
    {
        "vendor": "Metro Logistics",
        "invoice_number": "ML-7781",
        "date": "2026-06-12",
        "subtotal": 210.00,
        "tax": 21.00,
        "total": 231.00,
        "category": "logistics",
        "line_items": [
            {
                "description": "Courier service",
                "quantity": 6,
                "price": 35.00,
                "total": 210.00,
            },
        ],
    },
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Seed demo invoices into SQLite.")
    parser.add_argument("--database", help="Optional SQLite path for this run.")
    args = parser.parse_args()

    if args.database:
        os.environ["DATABASE_URL"] = f"sqlite:///{args.database}"

    from app.db.database import init_db
    from app.db.repository import create_invoice

    init_db()
    for invoice in SAMPLE_INVOICES:
        create_invoice(invoice, image_path="data/uploads/sample.png")

    print(f"Seeded {len(SAMPLE_INVOICES)} sample invoices.")


if __name__ == "__main__":
    main()
