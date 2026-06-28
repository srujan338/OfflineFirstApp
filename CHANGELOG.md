# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] — 2026-06-28

### Added

- **Project scaffolding** — README, SPEC, CONTRIBUTING, CHANGELOG, LICENSE, CLAUDE.md, CI workflow
- **Design system** — Color tokens, typography scale, spacing system (from SPEC.md)
- **PWA setup** — vite-plugin-pwa configuration, manifest, service worker
- **Dexie.js schema** — `receipts`, `pending`, `settings` stores
- **Zustand store** — `receiptStore` with Dexie.js persist middleware
- **TypeScript interfaces** — `Receipt`, `PendingReceipt`, `Category`, `ScanResult`
- **App routes** — React Router v6 with Home, Scan, Review, Dashboard, ReceiptDetail, Settings
- **Base UI components** — Button, Input, Card (shadcn/ui), Lucide icons
- **CameraCapture component** — getUserMedia camera flow with permissions handling
- **FileUpload component** — Image + PDF upload with pdf.js first-page extraction
- **ProcessingIndicator** — 3-step animated progress (Detect → Read → Extract)
- **ReceiptForm component** — Full review/edit form with validation
- **ReceiptCard component** — Dashboard card with category badge + swipe actions
- **CategoryBadge component** — Colored pill chip per category
- **ConfidencePip component** — AI confidence progress bar
- **DateNavigator component** — Month prev/next with date navigation
- **Dashboard page** — Grouped receipts, category filter, search, sort
- **ReceiptDetail page** — View/edit single receipt
- **EmptyState component** — Contextual empty states with CTAs
- **Toast component** — Auto-dismiss notification system
- **Settings page** — Export CSV, Export JSON, Clear data, About
- **Transformers.js integration** — Local SLM inference for structured extraction
- **Tesseract.js integration** — OCR for raw text extraction as fallback
- **CI pipeline** — 12 checks: lint, type-check, test, build, format, security scan

### TODO (Not Yet Implemented)

- [ ] Actual AI model integration (placeholder code present, model TBD)
- [ ] PDF page extraction (pdf.js integration)
- [ ] Swipe gestures on ReceiptCard (swipe-to-edit, swipe-to-delete)
- [ ] Duplicate detection (same date + shop + total → warning)
- [ ] Export to CSV
- [ ] Import from JSON backup
- [ ] Playwright E2E tests
- [ ] Install-to-homescreen PWA prompt
- [ ] Streak / gamification features
- [ ] Multi-language receipt support