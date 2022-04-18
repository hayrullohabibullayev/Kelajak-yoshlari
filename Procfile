web: gunicorn kelajak_yoshlari.wsgi
release: python manage.py migrate 
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput

