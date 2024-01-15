"""
Local settings
"""
from .base import *  # noqa


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['hiroshifuu.xyz', ])
ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ['127.0.0.1']


# env-apps
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    'debug_toolbar',
]


# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = 'crkc9qd#3okx+w+x$0dbtj7-4ktqj8g-3xju^&xr&&4*5tk#6z'


# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(str(BASE_DIR), 'db.sqlite3'),
    }
}
