from django.contrib import admin

from .models import Artwork, Comment

# Register your models here.
admin.site.register(Artwork)
admin.site.register(Comment)
