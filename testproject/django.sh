#!/bin/bash
echo "Create migrations"
python manage.py makemigrations test
echo "========================="

echo "Migrate"
python manage.py migrate
echo "=========================="

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000