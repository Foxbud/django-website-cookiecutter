from django.conf import settings
from django.core.validators import MinLengthValidator, RegexValidator


validate_username_chars = RegexValidator(
	regex=r'^[a-zA-Z0-9_-]*$',
	message=(
		'Only alphanumeric characters, underscores, '
		'and hyphens are allowed.'
	)
)


validate_username_min_len = MinLengthValidator(
	limit_value=settings.USERNAME_MIN_LEN,
	message=(
		'Must be at least '
		+ str(settings.USERNAME_MIN_LEN) +
		' characters.'
	)
)
