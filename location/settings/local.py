from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_CREDENTIALS = False
CSRF_TRUSTED_ORIGINS = [
    'http://*',
    'https://*',
]
CORS_ALLOWED_ORIGINS = [
    'http://*',
    'https://*',
]

# Apps
LOCAL_APPS = []
INSTALLED_APPS += LOCAL_APPS

# Database sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / f'{get_secret("DB_NAME_LOCAL")}.sqlite3',
    }
}
# Use for postgres db
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': get_secret('DB_NAME_LOCAL'),
#         'USER': get_secret('DB_USER_LOCAL'),
#         'PASSWORD': get_secret('DB_PASSWORD_LOCAL'),
#         'HOST': get_secret('DB_HOST_LOCAL'),
#         'PORT': get_secret('DB_PORT_LOCAL'),
#     }
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'