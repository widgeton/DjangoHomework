from django.core.management.base import BaseCommand
from hw_app.models import Order, Product


class Command(BaseCommand):
    help = 'Change products in order'

    def add_arguments(self, parser):
        parser.add_argument('id', help='Order ID')
        parser.add_argument('-a', '--add', type=int, nargs='*', help='Product IDs to add')
        parser.add_argument('-r', '--remove', type=int, nargs='*', help='Product IDs to remove')

    def handle(self, *args, **options):
        order = Order.objects.filter(pk=options['id']).first()
        if order is not None:
            for pk in options['remove']:
                product = Product.objects.filter(pk=pk).first()
                if product is not None:
                    order.common_price -= product.price
                    order.products.remove(product)

            for pk in options['add']:
                product = Product.objects.filter(pk=pk).first()
                if product is not None:
                    order.common_price += product.price
                    order.products.add(product)
