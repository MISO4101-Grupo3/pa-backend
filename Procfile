release: python manage.py makemigrations && python manage.py migrate
web: gunicorn MISO4101.wsgi --log-file -