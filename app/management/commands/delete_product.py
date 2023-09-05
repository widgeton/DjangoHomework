from django.core.management.base import BaseCommand
from hw_app.models import Product


class Command(BaseCommand):
    help = 'Create product'

    def add_arguments(self, parser):
        parser.add_argument('id')

    def handle(self, *args, **options):
        product = Product.objects.filter(pk=options['id']).first()
        if product is not None:
            product.delete()
