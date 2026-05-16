# ── Stage 1: Frontend builder ─────────────────────────────────────────────────
FROM node:20-slim AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

# ── Stage 2: Python dependency builder ────────────────────────────────────────
FROM python:3.11-slim AS builder
WORKDIR /build
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
        g++ \
    && rm -rf /var/lib/apt/lists/*
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ── Stage 3: Lean runtime image ───────────────────────────────────────────────
FROM python:3.11-slim
WORKDIR /app

# Copy installed Python packages
COPY --from=builder /install /usr/local

# Copy backend app source
COPY backend/app.py .

# Copy pre-trained ML artefacts
COPY models/ ./models/
COPY api/segmentation_insights.json ./api/segmentation_insights.json
COPY api/preprocessor_config.json   ./api/preprocessor_config.json

# Copy built frontend
COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

# Non-root user for security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]
