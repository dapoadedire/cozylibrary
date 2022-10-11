release: python manage.py makemigrations
release: python manage.py collectstatic
release: python manage.py migrate
web: gunicorn cozyproject.wsgi --log-file --
