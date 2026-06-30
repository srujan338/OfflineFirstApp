import cv2
from pathlib import Path

SUPPORTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}


def deskew_image(gray_img):
    """
    Deskew the image using minAreaRect on non-zero pixels
    """
    # Invert image to make text white on black background
    thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Find coordinates of all text pixels
    coords = cv2.findNonZero(thresh)
    if coords is None:
        return gray_img

    rect = cv2.minAreaRect(coords)
    angle = rect[-1]

    # Normalize the angle
    if angle < -45:
        angle = -(90 + angle)
    elif angle > 45:
        angle = 90 - angle

    # Only rotate if the angle is significant but not extreme
    if 0.5 < abs(angle) < 20:
        h, w = gray_img.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(
            gray_img,
            M,
            (w, h),
            flags=cv2.INTER_CUBIC,
            borderMode=cv2.BORDER_REPLICATE,
        )
        return rotated

    return gray_img


def preprocess_image(image_path: str):
    """
    CPU-only image preprocessing for OCR improvement:
    - grayscale
    - noise removal
    - deskew (basic)
    - thresholding
    """
    suffix = Path(image_path).suffix.lower()
    if suffix not in SUPPORTED_IMAGE_EXTENSIONS:
        raise ValueError("OCR preprocessing supports PNG and JPG invoice images")

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Invalid or unreadable image path")

    # 1. Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Noise reduction
    gray = cv2.medianBlur(gray, 3)

    # 3. Deskew (basic)
    gray = deskew_image(gray)

    # 4. Adaptive threshold (improves text visibility)
    processed = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2
    )

    return processed
