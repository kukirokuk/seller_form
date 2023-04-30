release: python manage.py migrate  --settings "settings_heroku"
web: gunicorn --env DJANGO_SETTINGS_MODULE=settings_heroku seller_form.wsgi --log-file djagno.log