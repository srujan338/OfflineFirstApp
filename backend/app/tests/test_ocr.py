from app.services.ocr_service import run_ocr


def test_run_ocr_returns_string(monkeypatch, tmp_path):
    image_path = tmp_path / "invoice.png"
    image_path.write_bytes(b"mock-image")

    monkeypatch.setattr(
        "app.services.ocr_service.preprocess_image", lambda path: "image"
    )
    monkeypatch.setattr(
        "app.services.ocr_service.pytesseract.image_to_string",
        lambda image, config: "ACME Supplies\nInvoice #INV-1001\nTotal 123.45",
    )

    result = run_ocr(str(image_path))

    assert isinstance(result, str)
    assert "Invoice" in result
