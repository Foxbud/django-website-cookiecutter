from django.views.generic import TemplateView


class ExamplePageView(TemplateView):
	template_name = 'example_app/example_page.html'
