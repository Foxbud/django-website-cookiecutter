import os


# ----- BASE -----

DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_KEY', '')

BASE_DIR = os.path.dirname(
	os.path.dirname(
		os.path.abspath(
			__file__
		)
	)
)

WEB_DIR = os.environ.get('DJANGO_WEBROOT', '')

ALLOWED_HOSTS = [
	os.environ.get('DJANGO_DOMAIN', ''),
]

INSTALLED_APPS = [
	# Main website custom app.
	'apps.{{cookiecutter.project_slug}}',

	# Extra custom apps.
	'apps.hello',

	# Built-in Django apps.
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.humanize',
	'django.contrib.messages',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.staticfiles',

	# Third party apps.
	'django_waitress',
	'sass_processor',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apps.{{cookiecutter.project_slug}}.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates'),],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'apps.{{cookiecutter.project_slug}}.context_processors.website_details',
			],
		},
	},
]

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.environ.get('DJANGO_DATABASE', ''),
	}
}

WSGI_APPLICATION = 'wsgi.application'

SITE_ID = 1


# ----- LOCALIZATION -----

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.environ.get('DJANGO_TIMEZONE', '')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ----- STATIC AND MEDIA FILES -----

STATIC_ROOT = os.path.join(WEB_DIR, 'static')

MEDIA_ROOT = os.path.join(WEB_DIR, 'media')

STATIC_URL = '/static/'

STATICFILES_FINDERS = [
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'sass_processor.finders.CssFinder',
]

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]

SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'

SASS_PROCESSOR_INCLUDE_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'

FILE_UPLOAD_PERMISSIONS = 0o644


# ----- AUTHENTICATION AND AUTHORIZATION -----

AUTHENTICATION_BACKENDS = [
	'django.contrib.auth.backends.ModelBackend',
]

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

AUTH_USER_MODEL = '{{cookiecutter.project_slug}}.User'

LOGIN_URL = 'admin:login'

LOGIN_REDIRECT_URL = '/'

USERNAME_MIN_LEN = 3

USERNAME_MAX_LEN = 20
