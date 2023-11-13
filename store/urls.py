from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('product_list', ProductView.as_view(), name='product_list'),
    path('create_order', OrderCreateView.as_view(), name='create_order'),
    path('all_products', all_products, name='all_products'),
    path('products_by_tag', products_by_tag, name='products_by_tag'),
]