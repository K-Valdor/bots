# syntax=docker/dockerfile:1
FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY VERSION ./VERSION
ARG APP_VERSION=0.0.0
ENV APP_VERSION=${APP_VERSION} PYTHONUNBUFFERED=1 PIP_DISABLE_PIP_VERSION_CHECK=on
CMD ["python", "-m", "app.main"]
