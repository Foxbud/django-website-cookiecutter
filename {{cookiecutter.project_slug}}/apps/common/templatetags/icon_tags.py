from django import template


register = template.Library()


@register.inclusion_tag('common/snippets/icon.html')
def icon(icon):
	# Build context.
	return {
		'icon': icon,
	}
