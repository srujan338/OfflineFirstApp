# Contributing to ReceiptAI

🎉 Thank you for your interest in contributing! ReceiptAI is an open-source project built for the CPU-First, Offline-First AI hackathon. Every contribution — code, design, bug reports, documentation — is welcome.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Code Style](#code-style)
- [Commit Messages](#commit-messages)
- [Pull Request Workflow](#pull-request-workflow)
- [Testing](#testing)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you agree to uphold a welcoming, respectful environment for everyone.

---

## Getting Started

### Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Node.js | ≥ 18 | [nodejs.org](https://nodejs.org) |
| npm | ≥ 9 | Comes with Node.js |

### Fork & Clone

```bash
# 1. Fork the repo on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/receiptai.git
cd receiptai

# 3. Add the original repo as upstream
git remote add upstream https://github.com/ranjithrajv/receiptai.git

# 4. Install dependencies
npm install
```

---

## Development Setup

### Start Dev Server

```bash
npm run dev
# Runs at http://localhost:5173
# Hot module replacement enabled — changes reload instantly
```

### Build for Production

```bash
npm run build
# Output in dist/ — fully static, can be served by any static host
```

### Preview Production Build

```bash
npm run preview
# Serves dist/ locally at http://localhost:4173
```

---

## Project Structure

```
receiptai/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── ui/              # Base shadcn/ui components (Button, Input, etc.)
│   │   ├── CameraCapture.tsx
│   │   ├── FileUpload.tsx
│   │   ├── ProcessingIndicator.tsx
│   │   ├── ReceiptForm.tsx
│   │   ├── ReceiptCard.tsx
│   │   ├── CategoryBadge.tsx
│   │   ├── ConfidencePip.tsx
│   │   ├── DateNavigator.tsx
│   │   ├── SearchBar.tsx
│   │   ├── EmptyState.tsx
│   │   └── Toast.tsx
│   ├── lib/                 # Core logic
│   │   ├── db.ts            # Dexie.js schema + all DB operations
│   │   ├── ai.ts            # Transformers.js pipeline wrapper
│   │   ├── ocr.ts           # Tesseract.js wrapper
│   │   └── types.ts        # TypeScript interfaces
│   ├── stores/
│   │   └── receiptStore.ts  # Zustand store with persist middleware
│   ├── pages/
│   │   ├── HomePage.tsx
│   │   ├── ScanPage.tsx
│   │   ├── ReviewPage.tsx
│   │   ├── DashboardPage.tsx
│   │   ├── ReceiptDetailPage.tsx
│   │   └── SettingsPage.tsx
│   ├── App.tsx              # Root component + router setup
│   └── main.tsx             # Entry point
├── public/                  # Static assets (PWA icons, etc.)
├── docs/                    # Additional docs
├── CLAUDE.md               # AI pair-programming context (don't edit)
├── SPEC.md                 # Feature specification (don't edit)
├── package.json
├── tsconfig.json
├── vite.config.ts
└── CONTRIBUTING.md          # This file
```

### Adding a New Component

1. Create `src/components/YourComponent.tsx`
2. Use TypeScript with explicit props interface
3. Follow the styling patterns in existing components (Tailwind + shadcn/ui base)
4. Export from `src/components/index.ts` if it's a shared component
5. Write unit tests in `src/components/__tests__/YourComponent.test.tsx`

---

## Code Style

### TypeScript

- **Strict mode** — no `any`, explicit types required
- Use `interface` for object shapes, `type` for unions/primitives
- Avoid type assertions (`as`) in production code

```typescript
// ✅ Good
interface ReceiptProps {
  receipt: Receipt;
  onEdit: (id: string) => void;
  onDelete: (id: string) => void;
}

// ❌ Avoid
const Receipt = (props: any) => { ... }
```

### React Patterns

- Functional components only (no class components)
- Use named exports for page components, default exports for shared UI components
- Keep components small — extract logic to custom hooks in `src/hooks/`
- Co-locate tests next to the file they test: `ReceiptCard.tsx` + `ReceiptCard.test.tsx`

### Tailwind CSS

- Use design system tokens from `SPEC.md` — don't invent new colors
- Prefer `className` over inline styles
- Use `cn()` utility from `lib/utils.ts` for conditional classes (shadcn pattern)

```typescript
// ✅ Good
<div className={cn(
  "rounded-lg border bg-white shadow-sm",
  isActive && "border-emerald-500",
  className
)}>

// ❌ Avoid
<div className="rounded-lg border bg-white shadow-sm" style={{ borderColor: isActive ? '#10B981' : '#e5e7eb' }}>
```

---

## Commit Messages

This project uses **Conventional Commits**. Your commit message title will be used as the PR title, so make it descriptive.

### Format

```
<type>(<scope>): <description>

[optional body]
[optional footer]
```

### Types

| Type | When to use |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, whitespace (no code change) |
| `refactor` | Code restructure without behavior change |
| `test` | Adding or updating tests |
| `chore` | Build scripts, CI, dependencies |
| `perf` | Performance improvements |
| `ci` | CI/CD changes |

### Examples

```
feat(dashboard): add category filter chips
fix(receipt-form): prevent negative total values
docs(readme): add quick start section
refactor(ai): extract model loading into separate hook
test(receipt-card): add swipe delete test
ci: add playwright e2e workflow
```

---

## Pull Request Workflow

### 1. Create a Branch

```bash
git checkout -b feat/your-feature-name
# or
git checkout -b fix/your-bug-description
```

### 2. Make Your Changes

```bash
git add .
git commit -m "feat(scope): describe your change"
```

### 3. Keep Up to Date

```bash
git fetch upstream
git rebase upstream/main
```

### 4. Run the Checklist

Before opening a PR, make sure ALL pass locally:

```bash
npm run lint           # ESLint + Prettier
npm run type-check    # TypeScript strict mode
npm run test          # Unit tests pass
npm run build         # Clean production build completes
```

**If any check fails, your PR will be blocked by CI.**

### 5. Open a Pull Request

1. Push your branch: `git push -u origin feat/your-feature-name`
2. Open a PR against `main`
3. Fill in the PR template
4. Link any relevant issues with `Closes #N` or `Ref #N`
5. Wait for CI to pass

### PR Template

```markdown
## Description
Brief summary of what this PR does.

## Type of Change
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 📝 Documentation update
- [ ] 🎨 UI/UX change
- [ ] 🔧 Configuration change

## Checklist
- [ ] Lint passes: `npm run lint`
- [ ] Type check passes: `npm run type-check`
- [ ] Tests pass: `npm run test`
- [ ] Build succeeds: `npm run build`
```

---

## Testing

### Unit Tests (Vitest)

```bash
# Run all tests
npm run test

# Run in watch mode
npm run test:watch

# Run with coverage
npm run test:coverage
```

### E2E Tests (Playwright)

```bash
# Install browsers
npx playwright install

# Run E2E tests (requires dev server running)
npm run dev &
npm run test:e2e
```

---

## Reporting Bugs

**Before submitting a bug report:**

1. Check existing issues — avoids duplicates
2. Try to reproduce on a fresh `npm install`

**When submitting, include:**
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots (if UI-related)
- Browser + OS + Node version

---

## Suggesting Features

Open a **Feature Request** issue (label: `enhancement`). Before opening:
- Check existing requests to avoid duplicates

**Feature requests should include:**
- Clear description of the feature
- Why it matters (user problem it solves)
- Possible alternatives considered

---

## 🙏 Thank You

Every contribution, no matter how small, makes this project better.