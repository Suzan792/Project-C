from django import template
from art.models import Artwork
from django.contrib.auth.models import User
from users.models import UserProfile
from products.models import Design

register = template.Library()

@register.simple_tag
def isLiked(art_pk, user_pk):
    art = Artwork.objects.get(pk=art_pk)
    if art.artwork_likes.filter(user_id=user_pk).exists():
        res = "text-danger"
    else:
        res = ""
    return res

@register.simple_tag
def isEditable(design_pk):
    design = Design.objects.get(pk=design_pk)
    if design.user==None:
        res = "false"
    else:
        res = "true"
    return res
