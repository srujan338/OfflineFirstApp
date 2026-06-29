# ReceiptAI — Specification

## 1. Concept & Vision

ReceiptAI is a privacy-first expense tracker that replaces the tedious work of manually logging receipts with a single photo. It feels like a modern banking app — calm, clean, trustworthy — except every byte stays on your device. The experience is frictionless: point, shoot, verify, done.

**Core feeling:** "My receipts are organized without me trying."

---

## 2. Design Language

### Aesthetic Direction
Minimal expense-tracker. Inspired by Linear.app and Walnut. Whitespace-forward, card-based, no visual clutter. Data-dense without feeling busy.

### Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `background` | `#FAFAFA` | Page background |
| `surface` | `#FFFFFF` | Cards, modals, inputs |
| `text-primary` | `#1A1A1A` | Headings, key data |
| `text-secondary` | `#6B7280` | Labels, metadata |
| `text-muted` | `#9CA3AF` | Placeholders, disabled |
| `accent` | `#10B981` | Positive values, CTAs |
| `warning` | `#F59E0B` | Alerts, medium confidence |
| `error` | `#EF4444` | Errors, delete actions |
| `border` | `#E5E7EB` | Card borders, dividers |
| `category-food` | `#F97316` | Food category tag |
| `category-rent` | `#8B5CF6` | Rent category tag |
| `category-shopping` | `#EC4899` | Shopping category tag |
| `category-transport` | `#3B82F6` | Transport category tag |
| `category-utilities` | `#14B8A6` | Utilities category tag |
| `category-other` | `#6B7280` | Other category tag |

### Typography

| Role | Font | Size / Weight |
|------|------|--------------|
| App name / Brand | Inter | 20px, font-semibold |
| Page heading | Inter | 24px, font-bold |
| Section heading | Inter | 16px, font-semibold |
| Body text | Inter | 14px, font-normal |
| Label | Inter | 12px, font-medium |
| Small/meta | Inter | 11px, font-normal |

### Spatial System

- Base unit: `4px`
- Padding (cards): `16px`
- Padding (sections): `24px`
- Gap (stack): `12px`
- Gap (grid): `16px`
- Border radius (card): `8px`
- Border radius (button): `6px`
- Border radius (chip/badge): `9999px` (pill)

### Motion

- **Card entrance:** fade-in + translateY(8px→0), 200ms ease-out
- **Button press:** scale(0.97), 100ms
- **Page transition:** opacity fade, 150ms
- **Loading states:** subtle pulse animation on skeleton
- **Confidence pip:** smooth width transition, 300ms

### Visual Assets

- Icons: **Lucide React** (consistent 24px, stroke-width 1.5)
- No external images required
- Category badges: solid pill chips with category color background
- Receipt thumbnails: stored as base64, max 300px wide

---

## 3. Layout & Structure

### Screen List

| Screen | Route | Description |
|--------|-------|-------------|
| Home | `/` | Entry point — camera + upload + recent receipts strip |
| Scan | `/scan` | Processing screen — shows captured image + AI extraction in progress |
| Review | `/review` | User corrects AI predictions before saving |
| Dashboard | `/dashboard` | Browse all verified receipts by date |
| Receipt Detail | `/receipt/:id` | View/edit single receipt |
| Settings | `/settings` | App preferences, export, about |

### Navigation

- Bottom navigation (mobile-first) with 3 tabs: **Home**, **Dashboard**, **Settings**
- No nested modals — each view is a route
- Swipe gestures on receipt cards: swipe-right to edit, swipe-left to delete

### Home Screen Layout

```
┌─────────────────────────────────┐
│  ReceiptAI            [⚙️]       │
├─────────────────────────────────┤
│                                 │
│    ┌───────────────────────┐   │
│    │   [📷 CAMERA CAPTURE]  │   │  ← Primary action (large, prominent)
│    │      Tap to scan       │   │
│    └───────────────────────┘   │
│                                 │
│    ─────── or ───────           │  ← Divider with text
│                                 │
│    [  📁 Upload a file  ]      │  ← Secondary action
│                                 │
├─────────────────────────────────┤
│  Recent Receipts                │  ← Section heading
│  ┌─────────────────────────┐   │
│  │ 🛒shop name    Rs.1,247  │   │  ← Mini receipt card
│  │ Jun 28, 2026  [Food]     │   │
│  └─────────────────────────┘   │
└─────────────────────────────────┘
│  🏠 Home  │  📊 Dashboard  │ ⚙️ │
└─────────────────────────────────┘
```

### Dashboard Screen Layout

```
┌─────────────────────────────────┐
│  Dashboard          [🔍] [≡]    │
├─────────────────────────────────┤
│  June 2026              ← →     │  ← Month navigator
│  Total: Rs. 23,450              │  ← Month total
├─────────────────────────────────┤
│  [All] [Food] [Rent] [🛒] [🚗]  │  ← Category filter chips
├─────────────────────────────────┤
│  Today — Jun 28                  │
│  ┌─────────────────────────┐   │
│  │ 🛒 Domino's Pizza        │   │
│  │ 2 items · Rs.1,247      │   │
│  │ Food · 🔄 Verified       │   │
│  └─────────────────────────┘   │
└─────────────────────────────────┘
```

---

## 4. Features & Interactions

### 4.1 Camera Capture

- Tap the camera area → request `getUserMedia()` permission
- On permission granted: show live camera preview with capture button
- On permission denied: show graceful message + link to settings
- Capture: take a still, freeze preview, show checkmark animation
- After capture: auto-navigate to `/scan` with the image

**States:** idle, loading, active, denied, captured

### 4.2 File Upload

- Tap "Upload a file" → trigger `<input type="file" accept="image/*,.pdf">`
- Accept: JPG, PNG, WEBP, HEIC, PDF
- PDF: extract first page as image using pdf.js
- On selection: show filename + size → navigate to `/scan` with file

**States:** idle, picking, selected, error

### 4.3 AI Processing (Scan Screen)

- Show the captured image as a large preview (sticky at top)
- Show processing state:
  - Step 1: "Detecting receipt..." (Tesseract initialization)
  - Step 2: "Reading text..." (OCR in progress)
  - Step 3: "Extracting data..." (Transformer.js inference)
- On complete: navigate to `/review` with extracted data
- On error: show error message with "Try Again" and "Enter Manually" options

### 4.4 Receipt Review Form

- Fields: Shop Name, Date, Transaction ID, Category, Items (list), Total, Notes
- All fields prefilled from AI extraction
- Validation:
  - Shop Name: required, min 2 chars
  - Date: required, valid date <= today
  - Total: required, positive number
  - Category: required (one of 6 categories)
- Inline validation on blur; errors shown below affected field
- "Save Receipt" button disabled until form valid

**Categories (radio chips):**
- 🍕 Food
- 🏠 Rent
- 🛒 Shopping
- 🚗 Transport
- 💡 Utilities
- 📦 Other

**Confidence indicator:**
- If AI confidence < 60%: yellow warning banner
- If confidence < 40%: red banner with double-check request

### 4.5 Save & Cancel

- **Save**: validates form → writes to Dexie.js → navigate to receipt detail with success toast
- **Skip/Save Later**: saves to "pending review" state → dashboard shows "⚠️" indicator
- **Discard**: asks "Are you sure?" → on confirm, navigate to Home, no data saved

### 4.6 Dashboard

- Default view: current month, all categories
- Receipts grouped by date (Today, Yesterday, then date)
- Each date group shows daily subtotal
- Bottom shows month total

**Filtering:** Category chips (multiselect) filter displayed receipts
**Month navigator:** ← prev / next → to change viewed month (cannot navigate to future)
**Search:** Debounced 300ms search across shop name, transaction ID, notes

### 4.7 Receipt Detail

- Full receipt card in read mode
- Tap "Edit" → fields become editable
- On save: updates Dexie.js record, shows success toast
- "Delete" → confirmation dialog → on confirm, deletes record, navigates to Dashboard

### 4.8 Settings Screen

- **Export Data**: Export all receipts as CSV
- **Export Data**: Export all receipts as JSON (for backup)
- **Import Data**: Import from JSON backup
- **Clear All Data**: Danger zone — "type DELETE to confirm" confirmation required
- **About**: Version, credits, license, hackathon link

---

## 5. Component Inventory

| Component | Description |
|-----------|-------------|
| `CameraCapture` | Full-screen camera view with capture button. States: idle, loading, active, denied, captured |
| `FileUpload` | Drag-and-drop or click-to-browse upload zone. States: idle, picking, selected, error |
| `ProcessingIndicator` | Animated 3-step progress (Detect → Read → Extract) with pulsing dots |
| `ReceiptForm` | Primary data-entry component. All fields for review/edit. Inline validation |
| `ReceiptCard` | Dashboard card. Shows shop icon, name, date, category badge, total. Swipeable |
| `CategoryBadge` | Pill chip with category name + color. Single-select in forms |
| `ConfidencePip` | Thin progress bar showing AI confidence (green ≥80%, yellow 60-79%, red <60%) |
| `DateNavigator` | Month header with prev/next arrows |
| `SearchBar` | Debounced search input with clear button |
| `EmptyState` | Illustrated empty states for no receipts / no results / no category matches |
| `Toast` | Auto-dismissing notification (3s). For saved, deleted, error, duplicate |

---

## 6. Technical Approach

### Framework & Build
- **React 18** with functional components + hooks
- **Vite** for dev server + build (fast refresh, optimized production builds)
- **TypeScript** strict mode throughout

### State Management
- **Zustand** for global state (receipts list, current scan, UI state)
- Persist middleware writes to Dexie.js on state changes

### Data Layer

**Dexie.js Schema:**
```typescript
db.version(1).stores({
  receipts: '++id, shopName, date, category, verified, createdAt, updatedAt',
  pending: '++id, tempId, date',
  settings: 'key'
});
```

### AI Pipeline

1. **Image Preprocessing** — resize to max 1024px wide, grayscale
2. **OCR** — Tesseract.js loads → extract raw text blocks
3. **Structured Extraction** — feed text to Transformers.js pipeline with extraction prompt
4. **Parse** — extract JSON from model output → populate form fields
5. **Confidence scoring** — model outputs confidence 0-1 → shown as ConfidencePip

### Routing

| Path | Component |
|------|-----------|
| `/` | `HomePage` |
| `/scan` | `ScanPage` |
| `/review` | `ReviewPage` |
| `/dashboard` | `DashboardPage` |
| `/receipt/:id` | `ReceiptDetailPage` |
| `/settings` | `SettingsPage` |

### Performance Targets
- First Contentful Paint: < 1.5s
- Time to Interactive: < 3s
- Model load time: < 10s (one-time, cached)
- Lighthouse PWA score: 100

---

## 7. Edge Cases & Error Handling

| Scenario | Behavior |
|----------|----------|
| Camera permission denied | Show explanation + "Open Settings" button |
| File upload fails | Toast with error, return to Home |
| AI processing fails | Error card with "Retry" and "Enter Manually" |
| Low storage quota | Alert user, offer to export + delete old receipts |
| Duplicate detected | Warning if same date + total + shop |
| No receipts | Empty state with camera CTA |
| Search returns nothing | "No receipts match" + clear button |
| Form invalid on save | Highlight invalid fields, scroll to first error |
| Delete confirmation | Modal with red "Delete" button; explicit tap required |

---

## 8. Accessibility

- All interactive elements keyboard accessible
- ARIA labels on icon-only buttons
- Focus trap in modals
- Color not sole indicator (category uses label + color)
- Minimum touch target: 44×44px
- Reduced motion respected via `prefers-reduced-motion`