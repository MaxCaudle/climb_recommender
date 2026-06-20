FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy repository into image so package `backend` is available at /app/backend
COPY . .

EXPOSE 8000

# Run FastAPI app via Gunicorn using Uvicorn worker
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "backend.api.main:app", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"]
