import os
import shutil
import logging
import pytesseract
from app.services.image_preprocess import preprocess_image
from app.utils.text_cleaning import clean_ocr_text

logger = logging.getLogger("invoice-intelligence.ocr")

TESSERACT_DEFAULT_WIN = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if os.path.exists(TESSERACT_DEFAULT_WIN):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_DEFAULT_WIN
    logger.info(f"Tesseract OCR found and configured at: {TESSERACT_DEFAULT_WIN}")
else:
    tesseract_in_path = shutil.which("tesseract")
    if tesseract_in_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_in_path
        logger.info(
            f"Tesseract OCR found in PATH and configured at: {tesseract_in_path}"
        )
    else:
        logger.warning(
            "CRITICAL WARNING: Tesseract OCR executable not found at "
            f"'{TESSERACT_DEFAULT_WIN}' or in system PATH. "
            "OCR pipeline WILL fail unless Tesseract is installed and configured."
        )


def run_ocr(image_path: str) -> str:
    """
    Extract raw text from invoice image using Tesseract OCR or pypdf for PDFs
    """
    suffix = os.path.splitext(image_path)[1].lower()
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader

            reader = PdfReader(image_path)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return clean_ocr_text(text)
        except Exception as e:
            logger.error(f"Error extracting text from PDF {image_path}: {e}")
            return ""

    processed_img = preprocess_image(image_path)

    # OCR configuration for better invoice extraction
    config = r"--oem 3 --psm 6"

    text = pytesseract.image_to_string(processed_img, config=config)
    return clean_ocr_text(text)
