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
	# Main website common app.
	'apps.common',

	# Extra custom apps.
	'apps.example_app',

	# Built-in Django apps.
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.flatpages',
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
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'apps.common.urls'

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
				'apps.common.context_processors.website_details',
				'apps.common.context_processors.theme',
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

USE_I18N = False

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

AUTH_USER_MODEL = 'common.User'

LOGIN_URL = 'admin:login'

LOGIN_REDIRECT_URL = '/'

USERNAME_MIN_LEN = 3

USERNAME_MAX_LEN = 20


# ----- THEMING -----

# Can be one of: sm, md, lg, or xl
THEME_CLASS_DESKTOP = 'lg'


# ----- MISC WEBSITE INFO -----

WEBSITE_DESCRIPTION = '{{cookiecutter.project_description}}'

WEBSITE_KEYWORDS = [
	'example',
	'keywords',
]

WEBSITE_AUTHOR = '{{cookiecutter.project_author}}'
