from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
	fieldsets = [
		(
			None,
			{
				'fields': [
					'username',
					'password',
				],
			},
		),
		(
			'Personal Info',
			{
				'fields': [
					'email',
				],
			},
		),
		(
			'Permissions',
			{
				'fields': [
					'is_active',
					'is_staff',
					'is_superuser',
					'groups',
					'user_permissions',
				],
			},
		),
		(
			'Important Dates',
			{
				'fields': [
					'last_login',
					'date_joined',
				],
			},
		),
	]
	list_filter = [
		'username',
		'email',
		'is_staff',
	]
	list_display = [
		'username',
		'email',
		'is_staff',
	]


admin.site.register(User, CustomUserAdmin)


# Set admin site title.
admin.site.site_title = admin.site.site_header = 'Management'
