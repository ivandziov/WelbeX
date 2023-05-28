#!/bin/sh
set -e

python manage.py makemigrations
python manage.py migrate
python export_data_about_location_to_db.py
python create_cars.py
python manage.py runserver 0.0.0.0:8000