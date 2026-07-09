# from django.contrib import admin
# from .models import Product

# # Register your models here.

# admin.site.register(Product)

from django.contrib import admin
from .models import Product, Order, OrderItem

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)