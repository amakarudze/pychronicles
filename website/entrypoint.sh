#!/bin/sh
set -e

if [ "$DJANGO_ENV" = "dev" ]; then
echo "Making migrations..."
python manage.py makemigrations core
fi

echo "Running migrations..."
python manage.py migrate --noinput

if [ "$DJANGO_ENV" = "prod" ]; then
  echo "Collecting static files..."
  python manage.py collectstatic --noinput

  echo "Starting Gunicorn..."
  exec gunicorn website.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
else
  echo "Starting Django dev server..."
  exec python manage.py runserver 0.0.0.0:8000
fi