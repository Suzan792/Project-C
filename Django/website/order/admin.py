from django.contrib import admin

from .models import OrderHistory, OrderDesign, OrderProduct, OrderArtwork

# Register your models here.
admin.site.register(OrderHistory)
admin.site.register(OrderDesign)
admin.site.register(OrderProduct)
admin.site.register(OrderArtwork)
