from django import template


register = template.Library()


@register.filter
def cat(val, arg):
	return str(val) + str(arg)
