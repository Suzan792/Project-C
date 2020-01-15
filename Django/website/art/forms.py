from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Comment


class uploadArt(forms.ModelForm):
    class Meta:
        model = models.Artwork
        fields = ['artwork_name','artwork_description','artwork_price','category','artwork_photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


