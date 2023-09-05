from django.core.management.base import BaseCommand
from hw_app.models import Product


class Command(BaseCommand):
    help = 'Create product'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', nargs='*', required=True)
        parser.add_argument('-d', '--description', nargs='*', required=True)
        parser.add_argument('-p', '--price', type=float, required=True)
        parser.add_argument('-a', '--amount', type=int, required=True)

    def handle(self, *args, **options):
        Product(name=' '.join(options['name']), description=' '.join(options['description']),
                price=options['price'], amount=options['amount']).save()
