# ===========================================================
# Stage 1 — Build the React frontend
# ===========================================================
FROM node:20-slim AS frontend-build

WORKDIR /app/frontend

# Cache npm install
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm install --legacy-peer-deps

COPY frontend/ ./
RUN npm run build

# ===========================================================
# Stage 2 — Python backend that also serves the built frontend
# ===========================================================
FROM python:3.10-slim

WORKDIR /app

# System deps for OCR + OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Python deps
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# App code
COPY backend/ ./

# Frontend build output (from stage 1)
COPY --from=frontend-build /app/frontend/dist /app/frontend/dist

# Persistent data directory
RUN mkdir -p /app/data/uploads

ENV DATA_DIR=/app/data \
    UPLOAD_DIR=/app/data/uploads \
    DATABASE_URL=sqlite:////app/data/invoices.db

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
