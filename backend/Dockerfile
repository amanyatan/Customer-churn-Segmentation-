# ── Stage 1: Dependency builder ───────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /build

RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
        g++ \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ── Stage 2: Lean runtime image ───────────────────────────────────────────────
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /install /usr/local

# Copy application source (build context = repo root)
COPY backend/app.py .

# Copy pre-trained ML artefacts
COPY models/ ./models/
COPY api/segmentation_insights.json ./api/segmentation_insights.json
COPY api/preprocessor_config.json   ./api/preprocessor_config.json

# Non-root user for security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Railway dynamically assigns $PORT
EXPOSE 8000

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]
