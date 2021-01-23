#!/usr/bin/env sh

python manage.py collectstatic --noinput
/app/.local/bin/uwsgi --http 0.0.0.0:8000 --module python_django_study.wsgi --master --processes 4 --threads 10