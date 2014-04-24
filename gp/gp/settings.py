# -*- encoding: utf-8 -*-

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from unipath import Path
PROJECT_DIR = Path(__file__).ancestor(2)
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_ROOT = PROJECT_DIR.child("static")

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    PROJECT_DIR.child("templates"),
)

SECRET_KEY = 'zi5y4+ovup(3+fg)jkd=_(oawzmxr+_4&nggjgnncj43jlx%g3'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'unipath',
    'django_extensions',
    'south',
    'crispy_forms',

    'core',

    'app.dominios',
    'app.proyectos',
    'app.tareas',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

GRAPPELLI_ADMIN_TITLE = 'Gestor de Proyectos Baética'
ROOT_URLCONF = 'gp.urls'
WSGI_APPLICATION = 'gp.wsgi.application'

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(PROJECT_DIR.ancestor(1), 'bd/db.sqlite3'),
    }
}

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True
