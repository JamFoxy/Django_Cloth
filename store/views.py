from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import *

from .forms import OrderForm

def sort_products_by_tag(request, tag_name):
    tag = get_object_or_404(TagCL, name=tag_name)
    products = ProductCL.objects.filter(tag=tag)
    context = {"products": products, "tag":tag}
    return render(request, "products_by_tag.html", context)

def show_error_page(request):
    return render(request, "error.html")

class ProductView(ListView):
    model = ProductCL
    queryset = ProductCL.objects.all()
    template_name = 'product_list.html'


class OrderCreateView(CreateView):
    model = OrderCL
    form_class = OrderForm
    success_url = '/'
    template_name = 'create_order.html'

