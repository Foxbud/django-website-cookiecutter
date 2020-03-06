import os

from .production import *


# ----- BASE -----

DEBUG = True

SECRET_KEY = '-i6_yr16cw^53mlhobk&16(wbd&0t&8xqma9b_rmrqa2ds*jrd'

TEMP_DIR = os.path.join(BASE_DIR, 'tmp')
# Create temp directory if necessary.
if not os.path.isdir(TEMP_DIR):
	os.mkdir(TEMP_DIR)

WEB_DIR = os.path.join(TEMP_DIR, 'webroot')

ALLOWED_HOSTS = [
	'localhost',
]

INSTALLED_APPS += [
	'debug_toolbar',
	'django_extensions',
]

MIDDLEWARE.insert(
	MIDDLEWARE.index('django.middleware.common.CommonMiddleware') + 1,
	'debug_toolbar.middleware.DebugToolbarMiddleware'
)

TEMPLATES[0]['OPTIONS']['context_processors'].append(
	'django.template.context_processors.debug'
)

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(TEMP_DIR, 'database.sqlite3'),
	}
}

INTERNAL_IPS = [
	'127.0.0.1',
]


# ----- LOCALIZATION -----

TIME_ZONE = '{{cookiecutter.development_timezone}}'


# ----- STATIC AND MEDIA FILES -----

STATIC_ROOT = os.path.join(WEB_DIR, 'static')

MEDIA_ROOT = os.path.join(WEB_DIR, 'media')
