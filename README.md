# InvoiceIQ

> **Offline AI-powered Invoice Data Extraction & Financial Schema Generation**

## Overview

InvoiceIQ is a CPU-first, offline AI application that extracts structured financial information from invoice images without requiring an internet connection.

The application detects invoices, recognizes text using OCR, extracts key financial fields, and converts the information into standardized JSON suitable for accounting systems.

## Problem Statement

Businesses receive hundreds of invoices every month. Manual data entry is time-consuming, error-prone, and often depends on cloud OCR services.

InvoiceIQ solves this by providing completely offline invoice processing powered by lightweight AI models that run efficiently on CPU.

## Features

- Invoice Detection
- OCR Text Extraction
- Table Detection
- Vendor Identification
- Invoice Number Extraction
- Date Detection
- GST/VAT Detection
- Currency Recognition
- Line Item Extraction
- Tax Calculation
- Total Amount Detection
- JSON & CSV Export
- Offline Processing

## Workflow

```text
Invoice Image
    │
    ▼
Image Enhancement
    │
    ▼
Table Detection
    │
    ▼
OCR
    │
    ▼
Field Extraction
    │
    ▼
Financial Schema Generator
    │
    ▼
JSON / CSV Export
```

## Sample JSON

```json
{
  "invoice_number": "INV-1023",
  "vendor_name": "ABC Traders",
  "invoice_date": "2026-06-28",
  "gst_number": "29ABCDE1234F1Z5",
  "currency": "INR",
  "items": [
    {
      "description": "Laptop",
      "quantity": 2,
      "unit_price": 45000,
      "total": 90000
    }
  ],
  "subtotal": 90000,
  "tax": 16200,
  "grand_total": 106200
}
```

## Tech Stack

- React + Vite
- Tailwind CSS
- TensorFlow Lite
- Tesseract.js
- OpenCV.js
- IndexedDB

## CPU-First

- Runs entirely on CPU
- No GPU/CUDA required

## Offline-First

- No cloud APIs
- No internet required
- All processing happens locally

## Project Structure

```text
invoiceiq/
├── frontend/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
└── CHANGELOG.md
```

## Installation

```bash
git clone https://gitlab.com/your-username/invoiceiq.git
cd invoiceiq
npm install
npm run dev
```

## Hackathon Compliance

| Requirement | Status |
|---|---|
| CPU-first | ✅ |
| Offline-first | ✅ |
| AI-powered | ✅ |
| No Cloud Calls | ✅ |
| Structured JSON Output | ✅ |
| Open Source | ✅ |

## License

GNU GPL v3.0
