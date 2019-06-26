web: python manage.py runserver
web: gunicorn mysite.wsgi:app --log-file -
heroku ps:scale web=1
