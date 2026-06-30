# InvoiceIQ Agent Guide

This document provides information for AI assistants, automation tools, and developers who want to programmatically interact with the InvoiceIQ system.

## Overview

InvoiceIQ is an offline-first invoice processing system built with:
- **Frontend**: React 18 + TypeScript + Vite
- **Backend**: FastAPI + Python 3.12+
- **Database**: SQLite (via sqlalchemy/sqlite-utils)
- **OCR Engine**: Tesseract.js (frontend) + pytesseract (backend)
- **AI Processing**: Regex-based parsing engine (no external ML APIs)

## System Architecture

```
┌─────────────────┐    ┌────────────────────┐    ┌─────────────────────┐
│   Frontend SPA  │◄──►│   RESTful API      │◄──►│   SQLite Database   │
│ (React/Vite)    │    │ (FastAPI/Python)   │    │ (invoiceiq.db)      │
└─────────────────┘    └────────────────────┘    └─────────────────────┘
        │                        ▲                        │
        │                        │                        │
        ▼                        │                        ▼
┌─────────────────┐    ┌────────────────────┐    ┌─────────────────────┐
|  User Interface |    |  OCR Processing    |    |  File Storage       |
| (Components)    │    | (Tesseract.js/py)  │    | (Uploads/ directory)│
└─────────────────┘    └────────────────────┘    └─────────────────────┘
```

## API Reference

All API endpoints are prefixed with `/api/v1` (configurable via `settings.API_V1_STR`).

### Base URL
- Development: `http://localhost:8000/api/v1`
- Production: Configured via reverse proxy or environment variables

### Authentication
Currently, the API does not require authentication for local use. In production deployments, consider adding:
- API key headers
- JWT tokens
- Basic auth via reverse proxy

### Standard Response Format
All successful responses follow this structure:
```json
{
  "success": true,
  "data": {...},          // Payload varies by endpoint
  "message": "Optional message"
}
```

Error responses:
```json
{
  "success": false,
  "detail": "Error description"
}
```

### Core Endpoints

#### Invoice Management

##### `POST /invoices/process`
Process an uploaded invoice file.

**Parameters:**
- `file` (multipart/form-data): The invoice image or PDF to process

**Returns:**
```json
{
  "success": true,
  "invoice_id": 123,
  "data": {
    "id": 123,
    "vendor": "Acme Corporation",
    "invoice_number": "INV-2024-001",
    "date": "2024-06-15",
    "subtotal": 100.00,
    "tax": 8.50,
    "total": 108.50,
    "currency": "USD",
    "category": "office",
    "line_items": [
      {
        "description": "Widget A",
        "quantity": 2,
        "unit_price": 25.00,
        "total": 50.00
      }
    ],
    "image_path": "data/uploads/abc123def456.jpg",
    "created_at": "2024-06-15 10:30:00"
  },
  "metrics": {
    "ocr_time": 0.234,
    "parse_time": 0.045,
    "total_time": 0.279,
    "memory_usage": 85.2
  }
}
```

##### `GET /invoices/`
Retrieve a paginated list of invoices.

**Query Parameters:**
- `limit` (int, default=50): Number of records to return
- `offset` (int, default=0): Number of records to skip

**Returns:**
```json
{
  "success": true,
  "data": [
    {
      "id": 123,
      "vendor": "Example Corp",
      "invoice_number": "INV-001",
      "date": "2024-06-10",
      "total": 75.50,
      "currency": "USD",
      "category": "supplies",
      "image_path": "data/uploads/xyz789.jpg",
      "created_at": "2024-06-10 14:22:00"
    }
  ]
}
```

##### `GET /invoices/{invoice_id}`
Get details for a specific invoice.

**Parameters:**
- `invoice_id` (path parameter): Integer ID of the invoice

**Returns:** Same format as individual item in list response above, plus `line_items` array.

##### `PUT /invoices/{invoice_id}/category`
Update the category for an invoice (used for learning).

**Parameters:**
- `invoice_id` (path parameter): Integer ID
- `category` (form/body): String category name

**Returns:**
```json
{
  "success": true,
  "message": "Category updated successfully"
}
```

#### Analytics Endpoints

##### `GET /analytics/expenditure`
Get spending summary by category.

**Returns:**
```json
{
  "success": true,
  "data": {
    "food": 234.56,
    "office": 128.90,
    "utilities": 87.33,
    "transport": 45.00,
    "other": 12.25
  }
}
```

##### `GET /analytics/runs`
Get processing performance metrics.

**Returns:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "invoice_id": 123,
      "ocr_time": 0.234,
      "parse_time": 0.045,
      "total_time": 0.279,
      "memory_usage": 85.2,
      "created_at": "2024-06-15 10:30:00"
    }
  ]
}
```

#### System Endpoints

##### `GET /`
Health check endpoint.

**Returns:**
```json
{
  "status": "ok",
  "message": "Invoice Intelligence API running on CPU"
}
```

## Data Models

### Invoice Model
| Field | Type | Description |
|-------|------|-------------|
| id | INTEGER | Primary key |
| vendor | TEXT | Supplier/company name |
| invoice_number | TEXT | Invoice identifier |
| date | TEXT | ISO date string (YYYY-MM-DD) |
| subtarget | REAL | Subtotal amount |
| tax | REAL | Tax amount |
| total | REAL | Total amount |
| currency | TEXT | ISO 4217 currency code (USD, EUR, etc.) |
| category | TEXT | Expense category |
| image_path | TEXT | Relative path to stored image |
| created_at | DATETIME | Timestamp of creation |
| line_items | JSON Array | Array of line item objects |

### Line Item Object
| Field | Type | Description |
|-------|------|-------------|
| description | TEXT | Item description |
| quantity | REAL | Quantity of items |
| unit_price | REAL | Price per unit |
| total | REAL | Quantity × unit_price |

### Processing Metrics
| Field | Type | Description |
|-------|------|-------------|
| ocr_time | FLOAT | Seconds spent on OCR |
| parse_time | FLOAT | Seconds spent on parsing/extraction |
| total_time | FLOAT | Total processing time |
| memory_usage | FLOAT | RAM usage in MB during processing |

## File Storage Structure

InvoiceIQ stores uploaded files in the `UPLOADS_DIR` (configurable via environment variable or `.env` file).

Default structure:
```
data/
├── uploads/
│   ├── 2024/
│   │   ├── 06/
│   │   │   ├── 15/
│   │   │   │   ├── abc123def456.jpg
│   │   │   │   └── xyz789ghi012.pdf
│   │   │   └── ...
│   │   └── ...
│   └── ...
└── invoiceiq.db
```

Files are named using UUIDs to avoid naming conflicts and preserve original extensions.

## Environment Configuration

Configuration is handled through environment variables or a `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | SQLite connection string | `sqlite:///./data/invoiceiq.db` |
| `DATA_DIR` | Base data directory | `./data` |
| `UPLOAD_DIR` | Uploads directory | `./data/uploads` |
| `MAX_UPLOAD_SIZE_MB` | Maximum file size (MB) | `10` |
| `API_V1_STR` | API version prefix | `/api/v1` |
| `PROJECT_NAME` | Application name | `Invoice Intelligence API` |

Example `.env` file:
```
DATABASE_URL=sqlite:///./data/invoiceiq.db
DATA_DIR=/var/lib/invoiceiq
UPLOAD_DIR=/var/lib/invoiceiq/uploads
MAX_UPLOAD_SIZE_MB=25
```

## Integration Examples

### Python Client
```python
import requests

def process_invoice(file_path):
    url = "http://localhost:8000/api/v1/invoices/process"
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
    return response.json()

def get_invoices(limit=100):
    url = f"http://localhost:8000/api/v1/invoices/?limit={limit}"
    response = requests.get(url)
    return response.json()

# Usage
result = process_invoice("invoice.pdf")
if result["success"]:
    invoice_id = result["invoice_id"]
    print(f"Processed invoice ID: {invoice_id}")
    
invoices = get_invoices()
print(f"Retrieved {len(invoices['data'])} invoices")
```

### Bash/cURL Examples
```bash
# Process an invoice
curl -X POST -F "file=@/path/to/invoice.jpg" \
  http://localhost:8000/api/v1/invoices/process

# Get all invoices
curl -s "http://localhost:8000/api/v1/invoices/?limit=10" | jq .

# Get spending by category
curl -s "http://localhost:8000/api/v1/analytics/expenditure" | jq .

# Update category
curl -X PUT -d "category=office" \
  http://localhost:8000/api/v1/invoices/123/category
```

### WebSocket / Real-time Features
Currently, InvoiceIQ does not use WebSockets for real-time updates. The frontend polls for updates or relies on full page refreshes after mutations. For real-time integrations:
1. Poll the `/invoices/` endpoint periodically
2. Listen for `storage` events if using localStorage sync
3. Implement webhook callbacks in your integration

## Error Handling

### Common HTTP Status Codes
- `200`: Success
- `400`: Bad Request (validation error, missing file, etc.)
- `404`: Not Found (invalid invoice ID)
- `413`: Payload Too Large (file exceeds MAX_UPLOAD_SIZE_MB)
- `500`: Internal Server Error (unexpected failure)
- `503`: Service Unavailable (temporary overload)

### Validation Errors
When submitting invalid data, you may receive:
```json
{
  "success": false,
  "detail": "Validation error: File type not supported",
  "errors": {
    "file": ["Only .jpg, .jpeg, .png, .bmp, .tiff, .pdf files are allowed"]
  }
}
```

## Rate Limiting & Performance

### Rate Limits
The API does not currently implement rate limiting for local use. For production deployments exposed to networks, consider implementing:
- Per-IP rate limiting via reverse proxy (NGINX, Travis)
- Request queuing for heavy processing operations
- Circuit breaker patterns for upstream dependencies

### Performance Characteristics
- **Single invoice processing**: Typically 0.5-3.0 seconds depending on image quality and size
- **Memory usage**: 50-150 MB per concurrent processing job
- **Throughput**: Limited by CPU cores; roughly (# cores) × 0.5 invoices/second
- **Database reads**: Very fast (<5ms for typical queries)
- **File I/O**: SSD recommended for best performance with frequent uploads

## Extending & Customizing

### Adding New Data Fields
To extract additional information from invoices:
1. Modify the regex patterns in `backend/services/pipeline_service.py`
2. Update the Pydantic models in `backend/schemas/`
3. Extend the database model in `backend/db/models.py`
4. Add frontend form fields in `frontend/src/components/InvoiceForm.tsx`
5. Update the database migration script if needed

### Custom Categories
To add expense categories beyond the defaults:
1. Edit `frontend/src/constants/categories.ts`
2. Add corresponding translations in `frontend/src/locales/` if using i18n
3. The backend stores categories as free-text strings, so no schema changes needed

### Alternative OCR Engines
While Tesseract is the default, you can integrate other OCR solutions:
1. Implement a new service interface in `backend/services/ocr_interface.py`
2. Create implementations for Tesseract, Google Vision, Azure Form Recognizer, etc.
3. Configure the active engine via environment variable
4. Ensure all implementations return the same standardized text format

### Multi-Language Support
The UI currently uses English as the default language. To add languages:
1. Add translation files to `frontend/src/locales/` (JSON format)
2. Register the new locale in `frontend/src/i18n/config.ts`
3. Update the language selector in `frontend/src/components/LanguageSelector.tsx`
4. OCR language selection is separate and handled in Settings

## Security Considerations

### Input Validation
All endpoints validate input:
- File type checking (extension + magic number verification)
- File size limits
- String length limits
- Numeric range validation
- Path traversal prevention

### Output Encoding
- API responses use JSON encoding with proper content types
- Frontend uses React's automatic XSS protection
- File names are sanitized before storage

### Dependencies & Supply Chain
- All Python packages are pinned in `requirements.txt`
- Node.js packages use exact versions in `package-lock.json`
- Regular security scanning recommended via:
  - `pip-audit` for Python dependencies
  - `npm audit` for Node.js dependencies
  - `safety` or `bandit` for Python security issues

## Monitoring & Observability

### Logging
Application logs are written to:
- `logs/app.log` (general application logs)
- `logs/errors.log` (error-level logs)
- `logs/access.log` (HTTP access logs - when enabled)

Log levels can be configured via:
```python
# In backend/core/logging.py
import logging
logging.basicConfig(level=logging.INFO)
```

### Metrics
Basic performance metrics are collected:
- Processing times per invoice
- Memory usage during processing
- Request latency and throughput
- Error rates and types

These are accessible via:
- `/api/v1/analytics/runs` endpoint
- Internal logging (when debug enabled)
- External monitoring via middleware hooks

### Health Checks
Beyond the root `/` endpoint:
- Database connectivity: Implicit in query responses
- Disk space: Monitor `DATA_DIR` and `UPLOAD_DIR` available space
- Memory usage: Track via system monitoring tools
- OCR availability: Test with known-good sample image

## Development & Testing

### Running Tests
```bash
# Backend tests
cd backend
python -m pytest tests/

# Frontend tests
cd ../frontend
npm test

# End-to-end tests (if configured)
npm run test:e2e
```

### Code Style
- **Python**: Black formatter, Ruff linter, MyPy type checking
- **JavaScript/TypeScript**: ESLint + Prettier
- **Commit messages**: Conventional Commits format

### Database Migrations
The current schema is initialized via `init_db()` in `backend/db/database.py`.
For schema changes:
1. Modify the SQL in `init_db()`
2. Update Pydantic models if needed
3. Ensure backward compatibility or provide migration scripts
4. Increment schema version in code comments

## Contact & Support

### For Developers
- **Issue Tracker**: [github.com/your-org/invoiceiq/issues](https://github.com/your-org/invoiceiq/issues)
- **Discussions**: [github.com/your-org/invoiceiq/discussions](https://github.com/your-org/invoiceiq/discussions)
- **Contributing Guide**: See [CONTRIBUTING.md](CONTRIBUTING.md)

### For Enterprise Users
- **Security Issues**: security@invoiceiq.example.com (PGP key available on request)
- **Licensing**: Commercial licenses available for modified distributions
- **Support SLA**: Available upon request for business accounts

---

*Document Version: 1.0.0*  
*API Version: v1*  
*Last Updated: July 2024*

*Note: This document describes the current stable release. Features and endpoints may change in future versions. Always refer to the inline API documentation at `/docs` when the server is running for the most accurate, version-specific information.*