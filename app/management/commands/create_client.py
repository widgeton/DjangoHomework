from django.core.management.base import BaseCommand
from hw_app.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', nargs='*', required=True)
        parser.add_argument('-p', '--phone', required=True)
        parser.add_argument('-e', '--email', required=True)
        parser.add_argument('-a', '--address', nargs='*', required=True)

    def handle(self, *args, **options):
        Client(name=' '.join(options['name']), email=options['email'],
               address=' '.join(options['address']), phone=options['phone']).save()
