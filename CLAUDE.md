---
name: receiptai-frontend
description: Invoice Reader - offline-first receipt scanning PWA built with React
owner: ranjithrajv
team: frontend-dev
technology: React 18 + Vite + Transformers.js + Dexie.js + Tailwind CSS
last_updated: 2026-06-28
---

# ReceiptAI — Frontend Context

ReceiptAI is an offline-first, CPU-optimized invoice/receipt reader that runs entirely in the browser. No server, no cloud calls, no GPU needed.

## What This App Does

1. **Import** — User opens the app → can snap a camera photo or upload a PDF/receipt image
2. **AI Reads** — Transformers.js (browser-native) extracts: shop name, date, transaction ID, line items, total cost, category
3. **User Reviews** — AI predictions shown in a clean form (not JSON). User can correct any misreads
4. **Save & Categorize** — Verified data stored in IndexedDB via Dexie.js, categorized as food / rent / shopping / other
5. **Dashboard** — Date-wise browseable list of all verified receipts; searchable, filterable

## Tech Stack (Frontend)

| Layer | Choice | Notes |
|-------|--------|-------|
| Framework | React 18 + Vite | Fast HMR, PWA plugin |
| Styling | Tailwind CSS + shadcn/ui | Minimal, accessible components |
| Icons | Lucide React | Clean, consistent |
| State | Zustand | Lightweight, minimal boilerplate |
| Offline DB | Dexie.js (IndexedDB) | Receipt persistence |
| AI/OCR | Transformers.js (HuggingFace) | Runs quantized SLM + Tesseract.js in WASM |
| PWA | vite-plugin-pwa | Offline shell, installable |
| Routing | React Router v6 | Works fully offline |
| Camera/Upload | Browser native APIs | No extra dependencies |

## App Structure (Frontend Only)

```
src/
├── components/
│   ├── ui/                  # shadcn/ui base components
│   ├── CameraCapture.tsx    # Camera access + photo capture
│   ├── FileUpload.tsx       # PDF/image upload
│   ├── ReceiptScanner.tsx   # AI processing screen
│   ├── ReceiptForm.tsx      # User review + correction form
│   ├── ReceiptCard.tsx      # Individual receipt in dashboard
│   ├── Dashboard.tsx        # Main receipt list view
│   ├── CategoryFilter.tsx   # Filter by food/rent/shopping/other
│   ├── DateNavigator.tsx    # Browse by date
│   └── Header.tsx           # App header
├── lib/
│   ├── db.ts                # Dexie.js schema + operations
│   ├── ai.ts                # Transformers.js pipeline wrapper
│   ├── ocr.ts               # Tesseract.js receipt extraction
│   └── types.ts             # TypeScript interfaces
├── stores/
│   └── receiptStore.ts      # Zustand store
├── pages/
│   ├── Home.tsx             # Upload + camera entry point
│   ├── Scan.tsx             # Processing + review
│   └── Dashboard.tsx         # Receipt browser
├── App.tsx
└── main.tsx
```

## Data Shape (stored in IndexedDB, never shown as JSON in UI)

```typescript
interface Receipt {
  id: string;                    // UUID
  shopName: string;              // e.g. "Domino's Pizza"
  date: string;                  // ISO date string
  transactionId: string;          // Bill/Invoice number
  items: { name: string; price: number }[];
  total: number;
  category: 'food' | 'rent' | 'shopping' | 'transport' | 'utilities' | 'other';
  confidence: number;             // AI confidence 0-1
  imageData?: string;             // Base64 thumbnail
  verified: boolean;
  notes?: string;
  createdAt: string;
  updatedAt: string;
}
```

## Key Design Decisions

### No JSON in UI
Data is always displayed as cards, form fields, and tables. Never raw JSON dumps to users.

### All-In-Browser AI
- `transformers` + `@huggingface/tfjs` runs a quantized model (~50-100MB, downloaded once)
- Model cached in browser IndexedDB storage
- All inference happens locally — no network calls for AI

### Offline-First
- App shell cached via Service Worker
- All data in IndexedDB (persists across restarts)
- Works completely air-gapped after first load

## Design System

- **Aesthetic**: Minimal expense-tracker. Clean whitespace, muted palette, one accent color.
- **Colors**:
  - Background: `#FAFAFA`
  - Surface: `#FFFFFF`
  - Text Primary: `#1A1A1A`
  - Text Muted: `#6B7280`
  - Accent: `#10B981` (emerald green)
  - Warning: `#F59E0B`
  - Error: `#EF4444`
- **Border radius**: 8px (cards), 6px (inputs)
- **Shadows**: Subtle, one level only (`shadow-sm`)

## Getting Started (Frontend Dev)

```bash
npm install
npm run dev         # development (http://localhost:5173)
npm run build       # production build
npm run lint        # ESLint
npm run type-check  # TypeScript
npm run test        # Vitest tests
```

## AI Model Note

Under hackathon CPU-first constraints, this app uses:
- **Transformers.js** with a quantized, CPU-optimized model
- **Tesseract.js** for raw OCR fallback
- No external API calls — all inference is 100% local

## Code Style

- TypeScript strict mode
- ESLint + Prettier (pre-commit hook)
- Conventional Commits (semantic PR titles)

## Designer Notes

- All monetary values: no currency symbol in UI. Use color coding instead.
- Confidence score shown as a subtle progress pip, not a number.
- Receipt cards: gentle entrance animation, no jarring transitions.