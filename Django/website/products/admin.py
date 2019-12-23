from django.contrib import admin

from .models import Product, Design , DesignArtCoordinate, DesignArtFrameCoordinate ,DesignTextCoordinate

# Register your models here.
admin.site.register(Product)
admin.site.register(Design)
admin.site.register(DesignArtCoordinate)
admin.site.register(DesignArtFrameCoordinate)
admin.site.register(DesignTextCoordinate)
