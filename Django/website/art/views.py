from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View
from art.models import Artwork
from products.models import Product
from django.utils import timezone
import json
from django.http import JsonResponse

# Create your views here.
class ArtDetailView(View):
    def get(self, request, *args, **kwargs):
        product_list = Product.objects.all()
        art = Artwork.objects.get(pk=self.kwargs.get('pk'))
        liked = False
        if request.user.is_authenticated:
            user = request.user.userprofile
            if art.artwork_likes.filter(id=user.id).exists():
                liked = True
        context = {
        'object': art,
        'product_list':product_list
        }
        return render(request, 'art/artwork_detail.html', context)
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            art = Artwork.objects.get(pk=self.kwargs.get('pk'))
            user = request.user.userprofile
            if art.artwork_likes.filter(id=user.id).exists():
                art.artwork_likes.remove(user)
                liked = False
            else:
                art.artwork_likes.add(user)
                liked = True
            like_count = art.artwork_likes.count()
            return JsonResponse({'liked':liked,'like_count':like_count})
