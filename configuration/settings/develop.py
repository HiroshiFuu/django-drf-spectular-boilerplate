"""
Develop settings
"""
from .base import *  # noqa


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = '4iz42d5!1xaw=noj$#v*&(fqaa*p7q1*j+(sq92ac%s&zvqz)u'


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
