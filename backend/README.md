# 🧠 Invoice Intelligence (CPU-First Offline AI)

> Turn invoices into structured financial data — completely offline, CPU-only.

---

## 🚀 Problem Statement

Most invoice processing systems:
- depend on cloud APIs
- require GPUs or internet
- fail in offline environments

We solve this by building a **fully offline, CPU-first AI pipeline**.

---

## ⚙️ Architecture

Image → Preprocessing (OpenCV)
→ OCR (Tesseract CPU)
→ Parsing Engine (Regex AI)
→ Category Intelligence
→ SQLite Storage
→ Analytics API

## 🧠 Key Features

- 📷 Invoice image → structured JSON
- 🧾 OCR using Tesseract (100% offline)
- ⚡ CPU-only processing pipeline
- 📊 Spending analytics by category
- 🧠 Adaptive vendor learning system
- 🗃 SQLite-based offline storage
- 📉 Performance tracking (CPU + memory)

---

## 🧰 Tech Stack

- FastAPI (Backend API)
- OpenCV (Image preprocessing)
- Tesseract OCR (CPU engine)
- SQLite (offline DB)
- Python (core logic)

---

## 📡 API Endpoints

### Process Invoice
POST /api/v1/invoices/process


### Get Invoices

GET /api/v1/invoices


### Get Invoice

GET /api/v1/invoices/{id}


### Update Category (Learning)

PUT /api/v1/invoices/{id}/category


### Analytics

GET /api/v1/analytics/expenditure


---

## 🔌 Offline Guarantee

✔ No cloud APIs  
✔ No external ML calls  
✔ Works with Wi-Fi OFF  
✔ Fully local SQLite storage  

---

## 📊 Metrics Tracked

- OCR time
- Parsing time
- Total processing time
- Memory usage per run

---

## 🧪 How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload