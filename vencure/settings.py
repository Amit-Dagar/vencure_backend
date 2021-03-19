"""
Django settings for vencure project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import dotenv
import datetime
import os

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

# CORS SECURITY
ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split()
CORS_ORIGIN_ALLOW_ALL = bool(os.environ['CORS_ORIGIN_ALLOW_ALL'])

# DOMAIN NAMES
BACKEND_DOMAIN = os.environ['BACKEND_DOMAIN']
ADMIN_DOMAIN = os.environ['ADMIN_DOMAIN']
VENDOR_DOMAIN = os.environ['VENDOR_DOMAIN']

AUTH_USER_MODEL = os.environ['AUTH_USER_MODEL']

# INSTALLED APPS DEFAULT/USER
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'vendor',
    'products',
    'agreements',
    'helper',
    'rest_framework',
    'rest_framework_jwt',
    'corsheaders',
]

# DEFAULT AUTH TOKEN CLASS
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}

# JWT AUTH TOKENS
JWT_AUTH = {
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=60 * 24),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}
JWT_SECRET = os.environ['JWT_SECRET']


# PAGINATION
PAGE_SIZE = 10


# GOOGLE RECAPTCHA KEYS
GOOGLE_VERIFY_RECAPTCHA_URL = os.environ['GOOGLE_VERIFY_RECAPTCHA_URL']
RECAPTCHA_SECRET_KEY = os.environ['RECAPTCHA_SECRET_KEY']


# EMAIL CONFIGURATIONS
# EMAIL_USE_TLS = bool(os.environ['EMAIL_USE_TLS'])
# EMAIL_HOST = os.environ['EMAIL_HOST']
# EMAIL_PORT = os.environ['EMAIL_PORT']
# EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

# MIDDLEWARE LAYERS
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = os.environ['ROOT_URLCONF']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = os.environ['WSGI_APPLICATION']


DATABASES = {
    'default': {
        'ENGINE': os.environ['DB_ENGINE'],
        'NAME': os.environ['DB_NAME'],
        "USER": os.environ['DB_USER'],
        "PASSWORD": os.environ['DB_PASSWORD'],
        "HOST": os.environ['DB_HOST']
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = os.environ["MEDIA_URL"]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = os.environ["STATIC_URL"]
