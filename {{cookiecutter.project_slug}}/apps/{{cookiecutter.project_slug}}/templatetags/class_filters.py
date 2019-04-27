from django import template


register = template.Library()


@register.filter
def cls(value):
	return value.__class__.__name__
