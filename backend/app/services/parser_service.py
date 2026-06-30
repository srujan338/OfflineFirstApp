import re
from app.utils.regex_patterns import DATE_PATTERNS, INVOICE_PATTERNS

# -------------------------
# HELPER FUNCTIONS
# -------------------------


def extract_first_match(patterns, text):
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group()
    return None


def extract_amounts(text):
    amounts = re.findall(r"\d+\.\d{2}", text)
    return [float(a) for a in amounts]


def extract_currency(text: str) -> str:
    # Common symbols and codes
    currency_map = {
        "$": "USD",
        "€": "EUR",
        "£": "GBP",
        "₹": "INR",
        "¥": "JPY",
        "USD": "USD",
        "EUR": "EUR",
        "GBP": "GBP",
        "INR": "INR",
    }
    for key, val in currency_map.items():
        if key in text:
            return val
    # Fallback/Default
    return "USD"


# -------------------------
# MAIN PARSER
# -------------------------


def parse_invoice_text(text: str):
    """
    Convert raw OCR text to structured invoice JSON
    CPU-friendly rule-based extraction
    """

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # -------------------------
    # 1. Vendor (usually first non-empty line)
    # -------------------------
    vendor = lines[0] if lines else "Unknown"

    # -------------------------
    # 2. Invoice Number
    # -------------------------
    invoice_number = "UNKNOWN"
    for pattern in INVOICE_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            matched_str = match.group()
            parts = re.split(r'[:#]', matched_str)
            if len(parts) > 1:
                invoice_number = parts[-1].strip()
            else:
                invoice_number = matched_str.strip()
            break

    # Fallback to simple line search if patterns failed
    if invoice_number == "UNKNOWN":
        for line in lines:
            if "invoice" in line.lower() or "inv" in line.lower():
                invoice_number = line
                break

    # -------------------------
    # 3. Date
    # -------------------------
    date = extract_first_match(DATE_PATTERNS, text) or "UNKNOWN"

    # -------------------------
    # 4. Amount extraction
    # -------------------------
    amounts = extract_amounts(text)

    subtotal = amounts[-3] if len(amounts) >= 3 else 0
    tax = amounts[-2] if len(amounts) >= 2 else 0
    total = amounts[-1] if len(amounts) >= 1 else 0

    # -------------------------
    # 5. Currency
    # -------------------------
    currency = extract_currency(text)

    # -------------------------
    # 6. Line Items (basic heuristic)
    # -------------------------
    line_items = []

    for line in lines:
        parts = line.split()
        if len(parts) >= 3:
            try:
                price = float(parts[-1])
                qty = float(parts[-2])
                desc = " ".join(parts[:-2])

                line_items.append(
                    {
                        "description": desc,
                        "quantity": qty,
                        "price": price,
                        "total": qty * price,
                    }
                )
            except (TypeError, ValueError):
                continue

    # -------------------------
    # FINAL STRUCTURE
    # -------------------------
    return {
        "vendor": vendor,
        "invoice_number": invoice_number,
        "date": date,
        "subtotal": subtotal,
        "tax": tax,
        "total": total,
        "currency": currency,
        "category": "other",
        "line_items": line_items,
    }
