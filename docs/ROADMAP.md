# ReceiptAI Roadmap

---

## 🚀 Phase 1 — MVP (Current)

> **Goal:** Ship a working receipt reader that works offline on CPU.

### In Progress
- [ ] Camera + upload capture flow
- [ ] AI model integration (Transformers.js)
- [ ] Review + correction form
- [ ] Dexie.js persistence
- [ ] Dashboard with date grouping
- [ ] Category filtering
- [ ] Export to CSV

### Done ✅
- [x] Project scaffolding (README, SPEC, CONTRIBUTING, CHANGELOG, LICENSE, CLAUDE.md)
- [x] CI pipeline (12 checks configured)
- [x] Design system tokens (colors, typography, spacing)
- [x] App routing structure
- [x] Base UI components

---

## 🔜 Phase 2 — Polish

> **Goal:** Better detection, smoother UX, fewer friction points.

### Planned
- [ ] **Receipt quality feedback** — "Hold steady" vs "Good angle" / "Too dark" guides after capture
- [ ] **Multi-receipt scan** — One photo with multiple small receipts splits into separate entries
- [ ] **Auto-categorization improvement** — Rule-based fallback when AI confidence is low
- [ ] **Duplicate detection** — Warn when same date + shop + total appears twice
- [ ] **Swipe gestures** — Swipe-right to edit, swipe-left to delete on receipt cards
- [ ] **Search** — Full-text search across shop name, transaction ID, notes
- [ ] **PDF upload** — Extract first page from PDF using pdf.js
- [ ] **Receipt thumbnails** — Show small image preview in card
- [ ] **Install prompt** — "Add to Home Screen" banner after 3rd receipt saved

---

## 🌟 Phase 3 — Intelligence

> **Goal:** Give users insights about their spending.

### Planned
- [ ] **Monthly summary card** — Total spent, top category, comparison to previous month
- [ ] **Budget setting** — Set monthly budgets per category; nudge at 80%, 100%
- [ ] **Weekly digest** — Friday: "You spent Rs.X this week. Food: 60%"
- [ ] **Spending streaks** — Days since last receipt logged; streak counter on home screen
- [ ] **Top shops** — "Your most-visited places" ranked list
- [ ] **Recurring subscription detection** — Auto-flag repeated charges

---

## 🌈 Phase 4 — Extensibility

> **Goal:** ReceiptAI data should be useful outside the app.

### Planned
- [ ] **JSON backup export** — Full database export for backup
- [ ] **JSON import** — Restore from backup
- [ ] **Export to Notion** — One-tap export to a Notion database
- [ ] **Tax-ready export** — Filter by category + date range → spreadsheet for tax filing

---

## 🌐 Phase 5 — Internationalization

### Planned
- [ ] **Multi-language OCR** — Hindi, Tamil, Telugu support
- [ ] **Language auto-detection** — Detect receipt language → apply correct OCR model
- [ ] **i18n (UI)** — Support UI in multiple languages (Hindi as first additional)
- [ ] **Multi-currency display** — User sets preferred currency

---

## 🔒 Phase 6 — Hardening

### Planned
- [ ] **Offline resilience testing** — Test suite for full air-gap scenarios
- [ ] **Storage quota management** — Proactive warning when IndexedDB approaches limits
- [ ] **Data migration** — Dexie.js schema versioning
- [ ] **Error boundaries** — React error boundaries so one component crash doesn't break app
- [ ] **Accessibility audit** — Full WCAG 2.1 AA audit

---

## 🎮 Future Ideas (Unsorted)

- [ ] **Receipt tagging** — "Client lunch", "Gift", "Business expense"
- [ ] **Photo gallery view** — Browse all receipts as a photo gallery
- [ ] **Voice notes** — Attach a short voice note to a receipt
- [ ] **Widget** — iOS/Android home screen widget showing monthly spend
- [ ] **Split bill** — For restaurant receipts, split total among N people
- [ ] **Tip calculator** — Detect and separate tip from restaurant receipts
- [ ] **AR receipt overlay** — Point camera at receipt → highlights fields in real-time