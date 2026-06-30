# Contributing

## Setup

Create a virtual environment and install the backend dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest black flake8 ruff mypy bandit pre-commit
pre-commit install
```

On Windows PowerShell, activate with:

```powershell
.venv\Scripts\Activate.ps1
```

## Running Locally

Initialize SQLite and start the FastAPI app:

```bash
python -c "from app.db.database import init_db; init_db()"
uvicorn app.main:app --reload
```

The service is CPU-only and offline-first. Keep all storage on SQLite and local files.

## Tests And Audit Checks

```bash
pytest app/tests
ruff check app scripts
black --check app scripts
flake8 app scripts
bandit -r app scripts -x app/tests
python scripts/benchmark_cpu.py
```

## Coding Standards

Keep changes small and focused. Do not add GPU-only dependencies, hosted databases, or network-based inference services. Use typed, readable Python and prefer deterministic rule-based behavior for audit-sensitive paths.
