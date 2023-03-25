"""Django settings for WhichPN project.
:note: Don't forget to replace '<stubs>' in `local_settings.py`
"""
from pathlib import Path
from typing import Dict
import os

BASE_DIR = Path(__file__).resolve().parent
ALLOWED_HOSTS = []
INSTALLED_APPS = ('core',)
MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'urls'
TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (os.path.join(BASE_DIR, 'templates'), ),
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ),
        },
    },
)
WSGI_APPLICATION = 'wsgi.application'
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

# == <stubs> ==
DEBUG = True
SECRET_KEY = 'secretkey'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
SPECIAL: Dict[str, int] = {}
# == </stubs> ==

try:
    from local_settings import *
except ImportError:
    pass
