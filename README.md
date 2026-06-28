# ReceiptAI

> **Turn paper receipts into clean, organized expense data — entirely on your CPU, entirely offline.**

ReceiptAI is an offline-first PWA that transforms photos of receipts and invoices into structured, categorized expense records. No cloud. No GPU. No signup.

[![CPU-First](https://img.shields.io/badge/CPU--First-Hackathon-10B981?style=flat-square)](https://github.com/ranjithrajv/awesome-cpu-first-ai)
[![Offline-First](https://img.shields.io/badge/Offline--First-Yes-10B981?style=flat-square)](https://offlinefirst.org/)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue?style=flat-square)](LICENSE)
[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-3178C6?style=flat-square)](https://www.typescriptlang.org/)

---

## ✨ Features

- 📷 **Snap or Upload** — Use your camera or import a PDF/photo of any receipt
- 🤖 **AI Reads the Receipt** — Local Transformer.js model extracts shop name, date, line items, total
- ✏️ **You Verify** — Review and correct AI predictions before saving
- 📅 **Browse by Date** — All receipts organized day-by-day in a clean dashboard
- 🏷️ **Auto-Categorize** — Food, Rent, Shopping, Transport, Utilities, Other
- 📴 **100% Offline** — Works without internet after first load
- 📱 **Installable PWA** — Add to your phone's home screen, runs like a native app
- 🔍 **Search** — Find receipts by shop name, category, or date range

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/your-org/receiptai.git
cd receiptai

# Install dependencies
npm install

# Start dev server (runs at http://localhost:5173)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

> **First load:** The AI model (~100MB) downloads once and is cached in your browser. After that, everything works offline.

---

## 🧠 How It Works

```
You snap a photo  →  Transformers.js runs locally  →  Data extracted
       ↓                                              ↓
  You review & correct  ←  Form displayed (NOT JSON)  ←  AI predictions
       ↓
  Saved to IndexedDB  →  Appears in Dashboard
```

### Step 1 — Capture
Open the app → tap **Camera** to snap a receipt, or **Upload** to select a file.

### Step 2 — AI Reads
The in-browser model extracts:
- Shop/vendor name
- Transaction date
- Bill/invoice number
- Line items with individual prices
- Total amount
- Suggested category

### Step 3 — You Verify
AI predictions appear in a clean form. Correct anything misread → tap **Save**.

### Step 4 — Organized Forever
Receipt appears in your Dashboard grouped by date. Filter by category, search by shop name.

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|------------|
| Framework | React 18 + Vite |
| Styling | Tailwind CSS + shadcn/ui |
| State | Zustand |
| Offline DB | Dexie.js (IndexedDB) |
| AI / OCR | Transformers.js (HuggingFace) + Tesseract.js |
| Icons | Lucide React |
| PWA | vite-plugin-pwa |
| Linting | ESLint + Prettier |
| Testing | Vitest + Playwright |

**AI Runtime:** All inference runs in-browser via WebAssembly. No external API calls. No GPU required.

---

## 📁 Project Structure

```
receiptai/
├── src/                      # React frontend source
│   ├── components/           # UI components (CameraCapture, ReceiptForm, etc.)
│   ├── lib/                  # Core logic (db.ts, ai.ts, ocr.ts)
│   ├── stores/               # Zustand state stores
│   ├── pages/                # Route pages (Home, Scan, Dashboard)
│   └── App.tsx
├── .github/workflows/        # CI pipeline
├── docs/                     # Additional documentation
├── CLAUDE.md                 # AI pair-programming context
├── SPEC.md                   # Detailed feature spec
├── CONTRIBUTING.md           # Dev setup guide
├── CHANGELOG.md              # Version history
└── LICENSE                   # AGPL-3.0
```

---

## 🧪 Running Tests

```bash
# Unit tests
npm run test

# Type check
npm run type-check

# Lint
npm run lint

# E2E tests (requires dev server running)
npm run test:e2e
```

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, code style, and PR workflow.

---

## 📄 License

**AGPL-3.0** — strong copyleft. This project is published under the GNU Affero General Public License v3. All contributions are subject to the same license.

See [LICENSE](LICENSE) for the full text.

---

## 🗺️ Roadmap

See [docs/ROADMAP.md](docs/ROADMAP.md) for planned features and future direction.

---

> *"The CPU is enough — and the best apps keep working when the network doesn't."*
>
> Built for the Local AI Hackathon — CPU-First, Offline-First.