import json
import os

from app.core.config import settings

# Simple persistent learning store (offline "mini-ML")
LEARNING_FILE = os.path.join(settings.DATA_DIR, "category_memory.json")


# -------------------------
# DEFAULT RULES
# -------------------------
CATEGORY_RULES = {
    "food": [
        "restaurant",
        "restaurants",
        "cafe",
        "coffee",
        "pizza",
        "mcdonald",
        "kfc",
        "swiggy",
        "zomato",
        "supermarket",
    ],
    "shopping": ["amazon", "walmart", "flipkart", "target", "mall"],
    "transport": ["petrol", "gas", "uber", "ola", "fuel", "shell"],
    "utilities": ["electricity", "water", "internet", "gas bill", "utility"],
    "health": ["pharmacy", "medical", "hospital", "clinic", "apollo"],
}


# -------------------------
# LOAD LEARNED DATA
# -------------------------
def load_memory():
    if not os.path.exists(LEARNING_FILE):
        return {}

    try:
        with open(LEARNING_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def save_memory(data):
    os.makedirs(os.path.dirname(LEARNING_FILE), exist_ok=True)
    with open(LEARNING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# -------------------------
# MAIN CLASSIFIER
# -------------------------
def categorize_vendor(vendor: str):
    vendor_lower = (vendor or "").lower()

    # 1. Check learned overrides first (user corrections)
    memory = load_memory()
    if vendor_lower in memory:
        return memory[vendor_lower]

    # 2. Rule-based matching
    for category, keywords in CATEGORY_RULES.items():
        for keyword in keywords:
            if keyword in vendor_lower:
                return category

    # 3. fallback
    return "other"


# -------------------------
# LEARNING FROM USER CORRECTION
# -------------------------
def update_category(vendor: str, category: str):
    memory = load_memory()
    memory[(vendor or "").lower()] = category
    save_memory(memory)

    return True
