from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_process_invoice_endpoint(monkeypatch):
    from app.api.routes import invoice_routes

    monkeypatch.setattr(
        invoice_routes,
        "process_invoice",
        lambda path: {
            "success": True,
            "invoice_id": 1,
            "data": {"vendor": "ACME Supplies", "total": 38.5},
            "metrics": {
                "ocr_time": 0.01,
                "parse_time": 0.01,
                "total_time": 0.02,
                "memory": 64.0,
            },
        },
    )

    response = client.post(
        "/api/v1/invoices/process",
        files={"file": ("invoice.png", b"image-bytes", "image/png")},
    )

    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["invoice_id"] == 1
    assert "memory" in response.json()["metrics"]


def test_list_invoices_endpoint(monkeypatch):
    from app.api.routes import invoice_routes

    monkeypatch.setattr(
        invoice_routes,
        "get_all_invoices",
        lambda limit, offset: [{"id": 1, "vendor": "ACME Supplies", "total": 38.5}],
    )

    response = client.get("/api/v1/invoices/")

    assert response.status_code == 200
    assert response.json()["data"][0]["vendor"] == "ACME Supplies"


def test_get_invoice_by_id_endpoint(monkeypatch):
    from app.api.routes import invoice_routes

    monkeypatch.setattr(
        invoice_routes,
        "get_invoice_by_id",
        lambda invoice_id: {
            "id": invoice_id,
            "vendor": "ACME Supplies",
            "line_items": [],
        },
    )

    response = client.get("/api/v1/invoices/1")

    assert response.status_code == 200
    assert response.json()["data"]["id"] == 1
