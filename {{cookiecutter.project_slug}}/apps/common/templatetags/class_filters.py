from django import template


register = template.Library()


@register.filter
def cls(val):
	return val.__class__.__name__
