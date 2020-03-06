from django import template
from django.urls import reverse


register = template.Library()


@register.inclusion_tag('common/snippets/button_row.html', takes_context=True)
def button_row(
		context,
		text,
		color,
		name='||',
		script='||',
		dest='||',
		dest_args='||'
):
	# Parse arguments.
	texts = str(text).split('|')
	colors = str(color).split('|')
	names = str(name).split('|')
	scripts = str(script).split('|')
	dests = str(dest).split('|')
	split_dest_args = [
		args.split(',')
		for args
		in str(dest_args).split('|')
	]

	# Reverse destination urls.
	for index in range(len(dests)):
		name = dests[index]
		args = split_dest_args[index]
		if name:
			if len(args) == 1 and not args[0]:
				dests[index] = reverse(dests[index])
			else:
				dests[index] = reverse(dests[index], args=args)

	# Calculate number of buttons.
	num = len(texts)

	# Build context.
	context.update(
		{
			'num_buttons': num,
			'buttons': [
				{
					'text': texts[button],
					'color': colors[button],
					'name': names[button],
					'script': scripts[button],
					'dest': dests[button],
				}
				for button
				in range(num)
			],
		}
	)

	return context
