from django.contrib.sites.shortcuts import get_current_site


def website_details(request):
	website = get_current_site(request)
	return {
		'website': {
			'domain': website.domain,
			'name': website.name,
		},
	}
