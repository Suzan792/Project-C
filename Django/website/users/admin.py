from django.contrib import admin
from .models import UserProfile , isArtist

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(isArtist)
