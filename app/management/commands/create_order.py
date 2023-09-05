from django.core.management.base import BaseCommand
from hw_app.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--client', type=int, required=True, help='Client ID')
        parser.add_argument('-p', '--products', nargs='*', type=int, required=True, help='List of product IDs')

    def handle(self, *args, **options):
        client = Client.objects.filter(pk=options['client']).first()
        products = []
        common_price = 0
        for pk in options['products']:
            product = Product.objects.filter(pk=pk).first()
            if product is not None:
                common_price += product.price
                products.append(product)

        if client is not None and products:
            order = Order(client=client, common_price=common_price)
            order.save()
            order.products.set(products)
