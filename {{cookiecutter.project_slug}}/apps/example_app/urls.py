from django.urls import path

from . import views


app_name = 'example_app'


urlpatterns = [
	path(
		'example_page/',
		views.ExamplePageView.as_view(),
		name='example_page'
	),
]
