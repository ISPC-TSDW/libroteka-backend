#!/bin/sh

wait-for-it ${MYSQL_PUBLIC_URL} --timeout=30

python manage.py migrate

exec gunicorn --bind 0.0.0.0:8000 Libroteka.wsgi:application