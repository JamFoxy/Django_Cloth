from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import *

from .forms import OrderForm

def all_products(request):
    products = ProductCL.objects.all()
    return render(request, 'all_products.html', {'products': products})


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
    tag = get_object_or_404(TagCL, name=tag_name)
    products = ProductCL.tags.filter(tag=tag)
    context = {'products': products, 'tag': tag}
    return render(request, 'products_by_tag.html', context)
