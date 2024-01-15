"""
Production settings
"""
from .base import *  # noqa


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['hiroshifuu.xyz', ])
ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ['10.0.0.1']

RUNSERVERPLUS_SERVER_ADDRESS_PORT = '0.0.0.0:8000'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGIN_REDIRECT_URL = '/MyTemplate'

FORCE_SCRIPT_NAME = '/MyTemplate'

STATIC_ROOT = '/app/STATIC_ROOT/static'
STATIC_URL = FORCE_SCRIPT_NAME + '/static/'
MEDIA_URL = FORCE_SCRIPT_NAME + '/media/'

DYNAMIC_LINK_URL_BASE_COMPONENT = 'OneTimeLink'
DYNAMIC_LINK_SCHEMA_PROTO = 'https'

SESSION_COOKIE_AGE = 60 * 10
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True

SCHEMA_VIEW_URL = 'https://hiroshifuu.xyz' + FORCE_SCRIPT_NAME


# env-apps
# ------------------------------------------------------------------------------
INSTALLED_APPS += [

]


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = ''


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# Uses django-environ to accept uri format
# See: https://django-environ.readthedocs.io/en/latest/#supported-types
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_POST'),
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True


# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(lineno)d %(message)s',
            'datefmt': '%Y/%b/%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/app/logs/debug.log',
            'backupCount': 30,
            'when': 'midnight',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'DEBUG',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'INFO',
        },
        'werkzeug': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
