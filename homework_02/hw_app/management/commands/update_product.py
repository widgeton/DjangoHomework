from django.core.management.base import BaseCommand
from hw_app.models import Product


class Command(BaseCommand):
    help = 'Update product'

    def add_arguments(self, parser):
        parser.add_argument('id')
        parser.add_argument('-n', '--name', nargs='*')
        parser.add_argument('-d', '--description', nargs='*')
        parser.add_argument('-p', '--price', type=float)
        parser.add_argument('-a', '--amount', type=int)

    def handle(self, *args, **options):
        product = Product.objects.filter(pk=options['id']).first()
        if product is not None:
            if options['name'] is not None:
                product.name = options['name']
            if options['description'] is not None:
                product.description = ' '.join(options['description'])
            if options['price'] is not None:
                product.price = options['price']
            if options['amount'] is not None:
                product.amount = options['amount']
            product.save()
