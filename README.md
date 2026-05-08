# 🧠 Customer Churn Intelligence System

A full-stack AI-powered dashboard for predicting and analyzing customer churn in European banking, built with **React + Vite** frontend and **FastAPI + XGBoost** backend.

## 🚀 Live Demo

Deployed on Vercel → *(add your URL after deployment)*

---

## ✨ Features

- **Dashboard Overview** — KPI cards, geography-based churn charts, age distribution pie chart
- **Segmentation Analytics** — Deep-dive into churn patterns across balance tiers, credit scores, age groups, and tenure
- **Predict Churn** — Enter individual customer details and get an AI risk score with probability
- **What-If Simulator** — Drag sliders to see how changes in customer attributes affect churn risk in real-time

## 🛠️ Tech Stack

| Layer      | Technology                          |
|------------|-------------------------------------|
| Frontend   | React 19, Vite 8, Tailwind CSS 4, Recharts |
| Backend    | FastAPI, Python 3.11                |
| ML Model   | XGBoost, Scikit-learn               |
| Deployment | Vercel (Static + Serverless Python) |

---

## 📂 Project Structure

```
├── api/                    # Vercel serverless function
│   ├── index.py            # FastAPI app with Mangum handler
│   └── requirements.txt    # Python deps for serverless
├── backend/                # Local dev backend
│   ├── app.py              # FastAPI server (local dev)
│   ├── pipeline.py         # ML training pipeline
│   └── requirements.txt    # Python deps (local)
├── frontend/               # React + Vite app
│   ├── src/
│   │   ├── pages/          # Dashboard, Segmentation, Prediction, Simulator
│   │   ├── App.jsx
│   │   └── index.css
│   └── vite.config.js
├── data/                   # Generated segmentation insights JSON
├── models/                 # Trained XGBoost model + preprocessor (.pkl)
├── vercel.json             # Vercel deployment configuration
└── README.md
```

---

## 🏗️ Local Development

### Prerequisites
- Node.js 18+
- Python 3.11+

### 1. Train the ML model
```bash
cd backend
pip install -r requirements.txt
python pipeline.py
```

### 2. Start the backend
```bash
cd backend
uvicorn app:app --reload
# Runs on http://localhost:8000
```

### 3. Start the frontend
```bash
cd frontend
npm install
npm run dev
# Runs on http://localhost:5173
```

The Vite dev server proxies `/api/*` requests to `localhost:8000`.

---

## 🌐 Deploy to Vercel

1. Push this repo to GitHub
2. Go to [vercel.com](https://vercel.com) and import the repository
3. Vercel will auto-detect the config from `vercel.json`
4. Click **Deploy** — that's it!

The `api/` folder runs as a serverless Python function, and the React frontend is served as static files.

---

## 📊 Dataset

European Banking Customer Churn dataset with 10,000+ records covering demographics, financial profiles, and banking behaviour.

---

## 📄 License

MIT
