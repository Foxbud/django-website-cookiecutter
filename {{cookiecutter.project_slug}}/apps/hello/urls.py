from django.urls import path

from . import views


app_name = 'hello'


urlpatterns = [
	path(
		'',
		views.HelloWorldView.as_view(
			extra_context={
				'page_title': 'Hello',
			}
		),
		name='hello_world'
	),
]
