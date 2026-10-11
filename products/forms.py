from django import forms
from .models import Product, Supplier, Stock


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'quantity',
            'price',
            'supplier'
        ]


class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = [
            'name',
            'email',
            'phone',
            'address'
        ]


class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = [
            'product',
            'quantity'
        ]