from django.views.generic import TemplateView


class HelloWorldView(TemplateView):
	template_name = 'hello/hello_world.html'
