import argparse
import os
import sys
import time
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

SUPPORTED_IMAGES = {".png", ".jpg", ".jpeg"}


def discover_images(image_dir: Path) -> list[Path]:
    if not image_dir.exists():
        return []
    return [
        path for path in image_dir.iterdir() if path.suffix.lower() in SUPPORTED_IMAGES
    ]


def benchmark_parser_only() -> None:
    from app.services.metrics_service import get_memory_usage_mb
    from app.services.parser_service import parse_invoice_text

    sample_text = """
    ACME Supplies
    Invoice # INV-1001
    2026-06-28
    Printer Paper 2 10.00
    Subtotal 20.00
    Tax 2.00
    Total 22.00
    """
    start = time.perf_counter()
    parse_invoice_text(sample_text)
    parse_time = time.perf_counter() - start

    print("No sample images found; parser benchmark completed.")
    print(
        "ocr_time=0.000s parse_time={:.3f}s memory={:.2f}MB".format(
            parse_time,
            get_memory_usage_mb(),
        )
    )


def main() -> None:
    from app.db.database import init_db
    from app.services.pipeline_service import process_invoice

    parser = argparse.ArgumentParser(description="CPU benchmark for invoice pipeline.")
    parser.add_argument(
        "--image-dir", default="data/uploads", help="Directory of sample images."
    )
    args = parser.parse_args()

    init_db()
    images = discover_images(Path(args.image_dir))
    if not images:
        benchmark_parser_only()
        return

    for image_path in images:
        try:
            start = time.perf_counter()
            result = process_invoice(str(image_path))
            total_time = time.perf_counter() - start
            metrics = result["metrics"]
            print(f"file={image_path.name}")
            print(
                "ocr_time={ocr:.3f}s parse_time={parse:.3f}s total_time={total:.3f}s "
                "memory={memory:.2f}MB".format(
                    ocr=metrics["ocr_time"],
                    parse=metrics["parse_time"],
                    total=total_time,
                    memory=metrics["memory"],
                )
            )
        except Exception as e:
            print(f"file={image_path.name} - Failed to process: {e}")


if __name__ == "__main__":
    main()
