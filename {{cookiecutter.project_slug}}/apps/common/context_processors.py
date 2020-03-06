from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


def website_details(request):
	website = get_current_site(request)
	return {
		'website': {
			'domain': website.domain,
			'name': website.name,
			'scheme': ('http' if settings.DEBUG else 'https') + '://',
			'description': settings.WEBSITE_DESCRIPTION,
			'keyworks': settings.WEBSITE_KEYWORDS,
			'author': settings.WEBSITE_AUTHOR,
		},
	}


def theme(request):
	return {
		'theme': {
			'class': {
				'desktop': settings.THEME_CLASS_DESKTOP,
			},
		},
	}
