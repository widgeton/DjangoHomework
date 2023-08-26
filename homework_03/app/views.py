from django.shortcuts import render
from .models import Order
from datetime import date, timedelta
from typing import Literal


def index(request):
    return render(request, 'app/base.html')


def get_orders(request, client_id):
    orders = Order.objects.filter(client__pk=client_id)
    return render(request, 'app/orders.html', {'orders': orders})


def get_products(request, client_id, period: Literal['week', 'month', 'year']):
    dif = {'week': timedelta(days=7), 'month': timedelta(days=30), 'year': timedelta(days=365)}.get(period)
    orders = Order.objects.filter(client__pk=client_id, date__gte=date.today() - dif)
    products = set()
    for order in orders:
        for product in order.products.all():
            products.add(product)
    return render(request, 'app/products.html', {'products': products, 'period': period})
