from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('orders/<int:client_id>/', views.get_orders, name='orders'),
    path('products/<int:client_id>/<str:period>/', views.get_products, name='products'),
]
