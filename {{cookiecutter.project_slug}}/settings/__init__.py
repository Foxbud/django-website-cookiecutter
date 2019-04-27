import os

if os.environ.get('DJANGO_SETTINGS', 'development') == 'development':
	from .development import *
else:
	from .production import *
