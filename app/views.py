from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from typing import Literal
from datetime import timedelta, date

from . import models
from . import forms


def index(request):
    return render(request, 'app/base.html', )


def about(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>О себе</title>
    </head>
    <body>
        <h1>О себе</h1>
        <p>Здесь должна быть информация страницы "О себе".</p>
    </body>
    </html>
    """
    return HttpResponse(html)


def get_all_products(request):
    products = models.Product.objects.all()
    return render(request, 'app/all_products.html', {'products': products})


def change_product(request, product_id):
    product = models.Product.objects.filter(pk=product_id).first()
    form = forms.ProductForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        image = form.cleaned_data['image']
        if isinstance(image, bool):
            image = None
        if image is not None:
            fs = FileSystemStorage()
            fs.save(image.name, image)
        product.name = form.cleaned_data['name']
        product.description = form.cleaned_data['description']
        product.price = form.cleaned_data['price']
        product.amount = form.cleaned_data['amount']
        product.image = image
        product.save()
        return redirect('all_products')
    else:
        form = forms.ProductForm(initial={'name': product.name, 'description': product.description,
                                          'price': product.price, 'amount': product.amount, 'image': product.image})

    return render(request, 'app/change_product.html', {'form': form})


def get_orders(request, client_id):
    orders = models.Order.objects.filter(client__pk=client_id)
    return render(request, 'app/orders.html', {'orders': orders})


def get_products(request, client_id, period: Literal['week', 'month', 'year']):
    dif = {'week': timedelta(days=7), 'month': timedelta(days=30), 'year': timedelta(days=365)}.get(period)
    orders = models.Order.objects.filter(client__pk=client_id, date__gte=date.today() - dif)
    products = set()
    for order in orders:
        for product in order.products.all():
            products.add(product)
    return render(request, 'app/products.html', {'products': products, 'period': period})
