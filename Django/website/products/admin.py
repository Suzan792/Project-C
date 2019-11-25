from django.contrib import admin

from .models import Product, Order, Wish, Design

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Wish)
admin.site.register(Design)
