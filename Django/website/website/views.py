from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View
from art.models import Artwork
from django.utils import timezone
import json
from django.http import JsonResponse

def contact_page(request):
    return render(request,'contact.html')
class ArtListView(ListView):
    model = Artwork
    template_name = 'index.html'
    context_object_name = 'Artworks'
    ordering = ['-upload_date_time']
    paginate_by = 6
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            art_pk = request.POST.get('id', None)
            art = Artwork.objects.get(pk=art_pk)
            user = request.user.userprofile

            if art.artwork_likes.filter(id=user.id).exists():
                print(user.id)
                print("True")
                art.artwork_likes.remove(user)
                liked = False
            else:
                print(user.id)
                print("False")
                art.artwork_likes.add(user)
                liked = True
            like_count = art.artwork_likes.count()
            return JsonResponse({'liked':liked,'like_count':like_count,'art_pk':art_pk})

class ArtDetailView(View):
    def get(self, request, *args, **kwargs):
        user = request.user.userprofile
        art = Artwork.objects.get(pk=self.kwargs.get('pk'))
        liked = False
        if art.artwork_likes.filter(id=user.id).exists():
            liked = True
        context = {
        'object': art,
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
