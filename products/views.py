from django.shortcuts import render
from .models import Product, Service

def product_view(request):
    product_list = Product.objects.all()
    return render(request, "products/products.html", {'product_list': product_list} )
