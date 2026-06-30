DATE_PATTERNS = [
    r"\d{2}[/-]\d{2}[/-]\d{4}",
    r"\d{4}[/-]\d{2}[/-]\d{2}",
]

INVOICE_PATTERNS = [
    r"invoice\s*#\s*[\w-]+",
    r"inv\s*#\s*[\w-]+",
    r"invoice\s*number\s*:\s*[\w-]+",
]

AMOUNT_PATTERN = r"\d+\.\d{2}"
