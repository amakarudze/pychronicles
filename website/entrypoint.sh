#!/bin/sh
set -e

export PATH="$(poetry env info -p)/bin:$PATH"

POSTGRES_HOST="${POSTGRES_HOST:-website_db}" 
POSTGRES_PORT="${POSTGRES_PORT:-5432}"

echo "Waiting for Postgres database at $POSTGRES_HOST:$POSTGRES_PORT..."

until getent hosts "$POSTGRES_HOST" >/dev/null 2>&1; do
  echo "Postgres host $POSTGRES_HOST not found, retrying..."
  sleep 1
done

until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  echo "Postgres not ready at $POSTGRES_HOST:$POSTGRES_PORT, sleeping 1s..."
  sleep 1
done

echo "Postgres $POSTGRES_HOST is ready!"

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn website.wsgi:application --bind 0.0.0.0:8000
