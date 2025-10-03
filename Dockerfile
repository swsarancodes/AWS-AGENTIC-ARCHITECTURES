# syntax=docker/dockerfile:1.4

# ============================================================================
# AWS AGENTIC ARCHITECTURES - MULTI-STAGE DOCKERFILE
# ============================================================================
# This Dockerfile creates optimized production and development images
# for the AWS Bedrock-based agentic patterns application.
# ============================================================================

# ----------------------------------------------------------------------------
# Stage 1: Base Image with System Dependencies
# ----------------------------------------------------------------------------
FROM python:3.10-slim-bullseye AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_VERSION=1.7.1 \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    build-essential \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create application user for security
RUN useradd -m -u 1000 -s /bin/bash appuser && \
    mkdir -p /app /app/logs /app/data && \
    chown -R appuser:appuser /app

# Set working directory
WORKDIR /app

# ----------------------------------------------------------------------------
# Stage 2: Dependencies Installation
# ----------------------------------------------------------------------------
FROM base AS dependencies

# Install UV package manager for faster dependency resolution
RUN pip install uv==0.1.35

# Copy dependency files
COPY --chown=appuser:appuser requirements.txt pyproject.toml ./

# Install Python dependencies using UV
RUN uv pip install --system -r requirements.txt

# Install additional production dependencies
RUN pip install gunicorn==21.2.0 prometheus-client==0.19.0

# ----------------------------------------------------------------------------
# Stage 3: Development Image
# ----------------------------------------------------------------------------
FROM dependencies AS development

# Install development tools
RUN uv pip install --system \
    pytest==7.4.3 \
    pytest-asyncio==0.21.1 \
    pytest-cov==4.1.0 \
    black==23.12.1 \
    flake8==6.1.0 \
    mypy==1.7.1 \
    ipython==8.18.1 \
    jupyter==1.0.0 \
    debugpy==1.8.0

# Copy entire application
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Expose ports
EXPOSE 8000 5678

# Development command with hot reload
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--log-level", "debug"]

# ----------------------------------------------------------------------------
# Stage 4: Production Image (Default)
# ----------------------------------------------------------------------------
FROM dependencies AS production

# Copy only necessary application files
COPY --chown=appuser:appuser api ./api
COPY --chown=appuser:appuser patterns ./patterns
COPY --chown=appuser:appuser utils ./utils
COPY --chown=appuser:appuser security ./security
COPY --chown=appuser:appuser monitoring ./monitoring
COPY --chown=appuser:appuser evaluation ./evaluation

# Create necessary directories
RUN mkdir -p logs data temp

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Expose port
EXPOSE 8000

# Production startup with Gunicorn for better performance
CMD ["gunicorn", "api.main:app", \
     "--workers", "4", \
     "--worker-class", "uvicorn.workers.UvicornWorker", \
     "--bind", "0.0.0.0:8000", \
     "--timeout", "300", \
     "--keep-alive", "5", \
     "--log-level", "info", \
     "--access-logfile", "-", \
     "--error-logfile", "-"]

# ----------------------------------------------------------------------------
# Stage 5: Testing Image
# ----------------------------------------------------------------------------
FROM development AS testing

# Install test dependencies
RUN uv pip install --system \
    pytest-xdist==3.5.0 \
    pytest-mock==3.12.0 \
    coverage==7.3.4 \
    locust==2.20.0

# Copy test files
COPY --chown=appuser:appuser tests ./tests

# Run tests by default
CMD ["pytest", "tests/", "-v", "--cov=patterns", "--cov=api", "--cov-report=html", "--cov-report=term"]

# ----------------------------------------------------------------------------
# Build Instructions:
# ----------------------------------------------------------------------------
# Development:
#   docker build --target development -t agentic-patterns:dev .
#   docker run -p 8000:8000 -v $(pwd):/app agentic-patterns:dev
#
# Production:
#   docker build --target production -t agentic-patterns:latest .
#   docker run -p 8000:8000 agentic-patterns:latest
#
# Testing:
#   docker build --target testing -t agentic-patterns:test .
#   docker run agentic-patterns:test
#
# With Docker Compose:
#   docker-compose up --build
# ============================================================================
