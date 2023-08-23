from django.core.management.base import BaseCommand
from hw_app.models import Client


class Command(BaseCommand):
    help = 'Create product'

    def add_arguments(self, parser):
        parser.add_argument('id')

    def handle(self, *args, **options):
        client = Client.objects.filter(pk=options['id']).first()
        if client is not None:
            client.delete()
