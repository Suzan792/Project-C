from django import template
from art.models import Artwork
from django.contrib.auth.models import User
from users.models import UserProfile

register = template.Library()

@register.simple_tag
def isLiked(art_pk, user_pk):
    art = Artwork.objects.get(pk=art_pk)
    user = User.objects.filter(pk=user_pk)
    if art.artwork_likes.filter(id=user_pk).exists():
        res = "text-danger"
    else:
        res = ""
    return res
