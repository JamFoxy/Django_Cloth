from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', ProductView.as_view()),
    path('create_order', OrderCreateView.as_view(), name='create_order'),
]