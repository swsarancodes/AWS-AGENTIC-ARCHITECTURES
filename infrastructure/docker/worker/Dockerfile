FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt celery

COPY patterns/ ./patterns/
COPY utils/ ./utils/

CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]
