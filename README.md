# InvoiceIQ

> **Turn invoices into structured financial data — completely offline, CPU-only.**

---

## ✨ Features

- 📷 **Invoice Processing** — Upload invoice images or PDFs to extract structured data
- 🧠 **CPU-First AI** — Runs entirely on CPU using Tesseract OCR and rule-based parsing
- 📊 **Spending Analytics** — View expenses by category with visual charts
- 💾 **Offline Storage** — All data stored locally in SQLite database
- 🔍 **Search & Filter** — Find invoices by vendor, date, amount, or category
- 🏷️ **Smart Categorization** — Automatic expense categorization with user feedback learning
- 📄 **PDF & Image Support** — Process both image files and PDF documents
- 📈 **Performance Metrics** — Track OCR and processing times for optimization

---

## 🏗️ Architecture

```
Image/PDF → Preprocessing (OpenCV) → OCR (Tesseract) → Parsing Engine → 
Category Intelligence → SQLite Storage → Analytics API → Frontend
```

### Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | React 18 + Vite + TypeScript |
| **Styling** | Tailwind CSS |
| **State** | React Query (TanStack Query) |
| **Charts** | Recharts |
| **Backend** | FastAPI (Python) |
| **OCR Engine** | Tesseract via pytesseract |
| **Image Processing** | OpenCV-Python |
| **Database** | SQLite (via sqlite-utils) |
| **PDF Processing** | PyPDF2 |
| **Utilities** | Python-multipart, Python-dotenv, PSUtil |

---

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.12+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/invoiceiq.git
cd invoiceiq

# Install frontend dependencies
cd frontend
npm install

# Install backend dependencies  
cd ../backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Development Setup

```bash
# Start backend server (from backend directory)
source venv/bin/activate
uvicorn app.main:app --reload

# Start frontend dev server (from frontend directory, in new terminal)
cd frontend
npm run dev
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Production Build

```bash
# Build frontend
cd frontend
npm run build

# Build backend (Docker recommended for production)
# See Dockerfile in backend/
```

---

## 📁 Project Structure

```
invoiceiq/
├── frontend/                 # React + Vite frontend
│   ├── src/                  # Source code
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/            # Page components
│   │   ├── lib/              # Core logic & utilities
│   │   ├── stores/           # State management
│   │   ├── hooks/            # Custom React hooks
│   │   ├── services/         # API service layers
│   │   └── App.tsx           # Root component
│   ├── public/               # Static assets
│   ├── index.html            # HTML template
│   ├── vite.config.ts        # Vite configuration
│   ├── tsconfig.json         # TypeScript configuration
│   └── package.json          # Dependencies & scripts
├── backend/                  # FastAPI backend
│   ├── app/                  # Application code
│   │   ├── api/              # API route definitions
│   │   ├── core/             # Configuration, logging, error handling
│   │   ├── db/               # Database models & repository
│   │   ├── ml/               # Machine learning models (if any)
│   │   ├── services/         # Business logic (OCR, processing, etc.)
│   │   ├── schemas/          # Pydantic models
│   │   └── main.py           # Application entry point
│   ├── data/                 # SQLite database & uploads
│   ├── scripts/              # Utility scripts
│   ├── requirements.txt      # Python dependencies
│   └── Dockerfile            # Container definition
├── docs/                     # Documentation
│   └── ROADMAP.md            # Feature roadmap
├── .gitignore                # Git ignore rules
├── package.json              # Root package (workspace)
└── README.md                 # This file
```

---

## 🔧 API Endpoints

### Invoice Management
- `POST /api/v1/invoices/process` - Upload and process an invoice
- `GET /api/v1/invoices/` - List all invoices (with pagination)
- `GET /api/v1/invoices/{id}` - Get a specific invoice
- `PUT /api/v1/invoices/{id}/category` - Update invoice category (for learning)

### Analytics
- `GET /api/v1/analytics/expenditure` - Get spending breakdown by category

### Monitoring
- `GET /api/v1/runs/` - Get processing performance metrics

### Health
- `GET /` - Health check endpoint

---

## 🧪 Testing

```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests  
cd ../frontend
npm test

# Type checking
cd frontend
npm run type-check

# Linting
cd frontend
npm run lint
```

---

## 📄 License

This project is licensed under the **AGPL-3.0 License** - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

---

## 📚 Documentation

- [User Manual](USER_MANUAL.md) - Comprehensive guide for end-users
- [Agent Guide](AGENTS.md) - Information for AI assistants and automation tools
- [API Documentation](http://localhost:8000/docs) - Auto-generated Swagger UI (when running)
- [Development Guide](backend/CONTRIBUTING.md) - Backend-specific development instructions

---

## 🗺️ Roadmap

See [docs/ROADMAP.md](docs/ROADMAP.md) for planned features and future direction.

---

> *"Financial data sovereignty starts with owning your own receipts."*  
> Built for privacy-conscious individuals and small businesses who need reliable, offline invoice processing.