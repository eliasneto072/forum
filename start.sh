#!/usr/bin/env sh
set -e

echo "Running migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if not exists..."
python manage.py shell <<'EOF'
from django.contrib.auth import get_user_model
User = get_user_model()

username = "eliasadmin083"
email = "admin@aeroforum.com"
password = "eliasnetodev083"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created")
else:
    print("Superuser already exists")
EOF

echo "Starting gunicorn..."
gunicorn studybud.wsgi:application --bind 0.0.0.0:${PORT:-8000}
