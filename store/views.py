from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import *

from .forms import OrderForm

def all_products(request):
    tags = TagCL.objects.all()
    return render(request, 'all_products.html', {'tags': tags})


class ProductView(ListView):
    model = ProductCL
    queryset = ProductCL.objects.all()
    template_name = 'product_list.html'


class TagsView(ListView):
    model = TagCL
    queryset = TagCL.objects.all()
    context_object_name = 'tags'
    template_name = 'all_products.html'


class OrderCreateView(CreateView):
    model = OrderCL
    form_class = OrderForm
    success_url = '/'
    template_name = 'create_order.html'


def products_by_tag(request, tag_name):
    products = ProductCL.objects.filter(tags__name__icontains=tag_name)
    context = {'products': products, 'tag': tag_name}
    return render(request, 'products_by_tag.html', context)
