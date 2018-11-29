#!/bin/bash
python manage.py makemigrations
python manage.py migrate
heroku config:set DISABLE_COLLECTSTATIC=1