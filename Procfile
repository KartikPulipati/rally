web: python manage.py migrate && gunicorn -b 0.0.0.0:$PORT --max-requests 100 --workers 3 --threads 1 rally.wsgi
