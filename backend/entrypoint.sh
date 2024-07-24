#!/bin/bash

# echo "Running collect static ..."
# python /opt/project/manage.py collectstatic --noinput

echo "Waiting for db ..."
until PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p 5432 -U $DB_USER -d $DB_NAME -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
echo "Connected to database"

python3 manage.py migrate --noinput
if [ $? -ne 0 ]; then
    echo "Migrate failed!" >&2
    exit 1
fi

python manage.py runserver 0.0.0.0:5000
# exec gunicorn --bind 0.0.0.0:80 --chdir /opt/project --log-level='info' --log-file=- --workers $GUNICORN_WORKER project.wsgi:application