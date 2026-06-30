# InvoiceIQ Constitution

## Project Name
InvoiceIQ – Offline Invoice Intelligence

## Vision
InvoiceIQ is an AI-powered document intelligence system that extracts structured information from invoice images entirely offline using CPU-based models. The application prioritizes privacy, speed, and accessibility by eliminating dependency on cloud APIs or GPUs.

---

# Core Principles

## I. Offline First

The application must function completely without internet connectivity.

- No cloud OCR
- No cloud AI inference
- No online storage
- Local processing only

---

## II. CPU First

The software should run efficiently on standard CPUs.

- TensorFlow Lite
- ONNX Runtime (CPU)
- OpenCV
- EasyOCR / PaddleOCR

GPU acceleration is optional but not required.

---

## III. Privacy by Design

Invoice data is confidential.

Therefore,

- Images never leave the device.
- Data remains local unless user exports.
- No telemetry.
- No analytics collection.

---

## IV. Standardized Output

Every invoice should produce structured JSON using a fixed schema.

Example:

```json
{
  "vendor_name": "",
  "invoice_number": "",
  "invoice_date": "",
  "due_date": "",
  "items": [],
  "subtotal": 0,
  "tax": 0,
  "total": 0
}
```

---

## V. Modular Architecture

The system consists of independent modules.

- Image Preprocessing
- OCR
- Table Detection
- Field Extraction
- JSON Formatter
- Export Module

Each module should be independently testable.

---

## VI. Explainability

Users should understand extraction results.

The system must:

- Highlight extracted regions
- Show confidence score
- Allow corrections before export

---

## VII. Cross Platform

Supported platforms:

- Windows
- Linux
- macOS

Future:

- Android
- Raspberry Pi

---

## VIII. Maintainability

Code must follow

- PEP8
- Modular architecture
- REST standards
- Clear documentation

---

## IX. Export Support

Supported formats

- JSON
- CSV
- Excel (future)
- Accounting software integration (future)

---

## X. Open Source Friendly

Project structure should encourage contributions.

Every module requires

- Documentation
- Unit tests
- README