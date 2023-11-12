from django import forms
from .models import OrderCL, ProductCL

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderCL
        fields = '__all__'
