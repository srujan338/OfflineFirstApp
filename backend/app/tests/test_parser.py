from app.services.parser_service import parse_invoice_text


def test_parse_invoice_text_returns_structured_json():
    text = """
    ACME Supplies
    Invoice # INV-1001
    Date: 2026-06-28
    Paper 2 10.00
    Pens 5 3.00
    Subtotal 35.00
    Tax 3.50
    Total 38.50
    """

    result = parse_invoice_text(text)

    assert result["vendor"] == "ACME Supplies"
    assert "INV" in result["invoice_number"]
    assert result["date"] == "2026-06-28"
    assert result["subtotal"] == 35.00
    assert result["tax"] == 3.50
    assert result["total"] == 38.50
    assert isinstance(result["line_items"], list)
    assert result["line_items"][0]["description"] == "Paper"
