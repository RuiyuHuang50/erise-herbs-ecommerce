#!/usr/bin/env bash
# build.sh

set -o errexit  # exit on error

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

echo "Build completed successfully!"
echo "Use start command: gunicorn ecommerce.wsgi:application"