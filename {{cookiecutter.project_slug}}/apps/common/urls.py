from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView


app_name = 'common'


urlpatterns = [
	path(
		'',
		RedirectView.as_view(
			url=reverse_lazy('example_app:example_page'),
			permanent=not settings.DEBUG
		)
	),

	path('admin/', admin.site.urls),

	path('example_app/', include('apps.example_app.urls')),
]


if settings.DEBUG:
	import debug_toolbar

	urlpatterns += static(
		settings.STATIC_URL,
		document_root=settings.STATIC_ROOT
	)
	urlpatterns += static(
		settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT
	)
	urlpatterns += [
		path('__debug__/', include(debug_toolbar.urls)),
	]
