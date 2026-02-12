FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Cria um script de start que roda migrate + collectstatic e inicia o gunicorn
RUN printf '%s\n' \
'#!/usr/bin/env sh' \
'set -e' \
'' \
'echo "Running migrations..."' \
'python manage.py migrate --noinput' \
'' \
'echo "Collecting static files..."' \
'python manage.py collectstatic --noinput' \
'' \
'echo "Starting gunicorn..."' \
'gunicorn studybud.wsgi:application --bind 0.0.0.0:${PORT:-8000}' \
> /app/start.sh \
&& chmod +x /app/start.sh

EXPOSE 8000

CMD ["/app/start.sh"]
