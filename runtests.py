#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import django
from django.conf import settings
from django.core.management import call_command

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

django_version = django.VERSION[:2]

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)
if django_version >= (1, 10):
    middleware_settings_name = 'MIDDLEWARE'
else:
    middleware_settings_name = 'MIDDLEWARE_CLASSES'

opts = {
    'INSTALLED_APPS': [
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.auth',
        'redactor'],
    'ROOT_URLCONF': 'redactor.urls',
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':MEMORY:'}
    },
    middleware_settings_name: MIDDLEWARE
}

settings.configure(**opts)

if django_version >= (1, 7):
    django.setup()

if __name__ == "__main__":
    call_command('test', 'redactor')
