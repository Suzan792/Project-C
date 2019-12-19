from django.contrib import admin

from .models import Product, Order, Wish, Design , DesignArtCoordinate, DesignArtFrameCoordinate ,DesignTextCoordinate

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Wish)
admin.site.register(Design)
admin.site.register(DesignArtCoordinate)
admin.site.register(DesignArtFrameCoordinate)
admin.site.register(DesignTextCoordinate)
