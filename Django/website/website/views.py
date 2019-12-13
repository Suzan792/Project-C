from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View
from art.models import Artwork
from users.models import User, UserProfile
from advertisementSlide.models import AdvertisementSlide
from products.models import Product
from django.utils import timezone
import json
from django.http import JsonResponse


def about_page(request):
    return render(request,'about.html')
class ArtListView(ListView):
    model = Artwork
    template_name = 'index.html'
    context_object_name = 'Artworks'
    ordering = ['-upload_date_time']
    paginate_by = 12

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArtListView, self).get_context_data(**kwargs)
        context['newest'] = UserProfile.objects.filter(user_role = 'artist').order_by('activated_artist_date').reverse()[:4]
        context['advertisementSlides'] = AdvertisementSlide.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            art_pk = request.POST.get('id', None)
            art = Artwork.objects.get(pk=art_pk)
            user = request.user.userprofile

            if art.artwork_likes.filter(id=user.id).exists():
                art.artwork_likes.remove(user)
                liked = False
            else:
                art.artwork_likes.add(user)
                liked = True
            like_count = art.artwork_likes.count()
            return JsonResponse({'liked':liked,'like_count':like_count,'art_pk':art_pk})
