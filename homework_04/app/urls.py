from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all_products/', views.get_all_products, name='all_products'),
    path('change_product/<int:product_id>/', views.change_product, name='change_product'),
]
