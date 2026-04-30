# Customer Churn Intelligence System

A production-level, scalable, and responsive end-to-end Customer Churn Intelligence System using the European Banking dataset.

## System Architecture

The project is structured as a full-stack application combining a FastAPI backend, Scikit-learn/XGBoost Machine Learning pipeline, and a modern React (Vite) frontend with Tailwind CSS and Recharts.

- **Backend (`/backend`)**: FastAPI server that loads an XGBoost churn prediction model and serves segmentation data.
- **Frontend (`/frontend`)**: React.js (Vite) Single Page Application styled with TailwindCSS (glassmorphism) and Recharts for interactive dashboards.
- **Machine Learning (`/backend/pipeline.py`)**: Data ingestion, preprocessing, feature engineering, and model training script.
- **Data & Models (`/data`, `/models`)**: Store dataset, segmentation insights, and trained models (`xgboost_model.pkl`, `preprocessor.pkl`).

## 🚀 Features

- **Customer Segmentation**: Analytics showing churn by geography, age, credit score, and tenure.
- **Predictive Modeling**: High accuracy XGBoost classifier identifying high-risk customers based on behavioral and financial traits.
- **Interactive Dashboard**: Modern glassmorphism UI with real-time churn prediction forms and visualizations.
- **What-If Simulator**: Adjust parameters to observe real-time impact on the churn probability.

## 🛠️ Installation & Setup

You can run this project locally or using Docker.

### Running Locally

1. **Install Backend Dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Generate Models and Analytics**:
   Run the ML pipeline to generate `xgboost_model.pkl` and `segmentation_insights.json`.
   ```bash
   cd backend
   python pipeline.py
   ```

3. **Start the FastAPI Server**:
   ```bash
   cd backend
   python app.py
   ```
   The backend will be available at `http://localhost:8000`.

4. **Install Frontend Dependencies & Start React App**:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173`.

### Running with Docker

You can use Docker Compose to spin up both the frontend and backend in production mode.

```bash
docker-compose up --build
```
- Frontend will be accessible at `http://localhost:5173`
- Backend will be accessible at `http://localhost:8000`

---

