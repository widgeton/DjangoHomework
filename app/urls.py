from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
    path('orders/<int:client_id>/', views.get_orders, name='orders'),
    path('products/<int:client_id>/<slug:period>/', views.get_products, name='products'),
    path('all_products/', views.get_all_products, name='all_products'),
    path('change_product/<int:product_id>/', views.change_product, name='change_product'),
]
