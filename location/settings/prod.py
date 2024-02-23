from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_CREDENTIALS = False
CSRF_TRUSTED_ORIGINS = [
    'https://apilocation.omardanielesquivel.com',
]
CORS_ALLOWED_ORIGINS = [
    'http://*',
    'https://*',
]

# Apps
LOCAL_APPS = []
INSTALLED_APPS += LOCAL_APPS

# Database sqlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / f'{get_secret("DB_NAME_PROD")}.sqlite3',
#     }
# }
# Use for postgres db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME_PROD'),
        'USER': get_secret('DB_USER_PROD'),
        'PASSWORD': get_secret('DB_PASSWORD_PROD'),
        'HOST': get_secret('DB_HOST_PROD'),
        'PORT': get_secret('DB_PORT_PROD'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / STATIC_URL]
STATIC_ROOT = BASE_DIR / 'staticfiles/'