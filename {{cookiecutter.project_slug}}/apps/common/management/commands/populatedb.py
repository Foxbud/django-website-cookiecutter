from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	help = (
		'Populate the database with default objects. '
		'Perform at least one migration before using this command.'
	)

	def __init__(self):
		super().__init__()
		self.User = get_user_model()
		if settings.DEBUG:
			self.schema = 'http'
			self.domain = 'localhost:8000'
			self.site_name = '{{cookiecutter.project_name}} (Dev)'
		else:
			self.schema = 'https'
			self.domain = settings.ALLOWED_HOSTS[0]
			self.site_name = '{{cookiecutter.project_name}}'

	def handle(self, *args, **options):
		self.init_admin()
		self.init_site()

	def init_admin(self):
		try:
			self.admin = self.User.objects.get(username='admin')
			self.stderr.write(
				'User "admin" already exists.'
			)
		except self.User.DoesNotExist as e:
			self.admin = self.User.objects.create_superuser(
				'admin',
				'',
				'admin'
			)
			self.stdout.write(
				self.style.SUCCESS('Created superuser "admin".')
			)

	def init_site(self):
		try:
			self.site = Site.objects.get(name=self.site_name)
			self.stderr.write(
				'Site was already renamed.'
			)
		except Site.DoesNotExist as e:
			self.site = Site.objects.get(name='example.com')
			self.site.name = self.site_name
			self.site.domain = self.domain
			self.site.save()
			self.stdout.write(
				self.style.SUCCESS('Renamed site.')
			)
