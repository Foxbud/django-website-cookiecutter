from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView


app_name = '{{cookiecutter.project_slug}}'


urlpatterns = [
	path(
		'',
		RedirectView.as_view(
			url=reverse_lazy('hello:hello_world'),
			permanent=not settings.DEBUG
		)
	),

	path('hello/', include('apps.hello.urls')),

	path('admin/', admin.site.urls),
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
