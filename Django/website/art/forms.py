from django import forms
from django.contrib.auth.models import User
from . import models
class uploadArt(forms.ModelForm):
    class Meta:
        model = models.Artwork
        fields = ['artwork_name','artwork_description','artwork_photo']


