#!/usr/bin/env sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting gunicorn..."
gunicorn studybud.wsgi:application --bind 0.0.0.0:${PORT:-8000}