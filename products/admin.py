from django.contrib import admin

from .models import Product, Service

admin.site.register(Service)
admin.site.register(Product)