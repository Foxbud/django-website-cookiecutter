from django.conf import settings
from django.contrib.auth.models import (
	AbstractBaseUser,
	PermissionsMixin,
	UserManager
)
from django.db import models
from django.utils import timezone

from .validators import validate_username_min_len, validate_username_chars


class User(PermissionsMixin, AbstractBaseUser):
	username = models.CharField(
		max_length=settings.USERNAME_MAX_LEN,
		unique=True,
		validators=[
			validate_username_min_len,
			validate_username_chars,
		]
	)
	email = models.EmailField(blank=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now)
	last_login = models.DateTimeField(default=timezone.now)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	EMAIL_FIELD = 'email'

	REQUIRED_FIELDS = [
		'email',
	]
