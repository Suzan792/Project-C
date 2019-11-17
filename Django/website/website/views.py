from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View
from art.models import Artwork
from like_count.models import Like
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


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user.userprofile
            liked_art_list = []
            like_list = Like.objects.filter(user=user)
            for item in like_list:
                liked_art_list.append(item.art.id)

            context['liked_art_list'] = liked_art_list
        return context
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            art_pk = request.POST.get('id', None)
            art = Artwork.objects.get(pk=art_pk)
            user = request.user.userprofile

            if Like.objects.filter(user=user).filter(art=art).exists():
                Like.objects.filter(user=user).filter(art=art).delete()
                liked = False
            else:
                like_instance = Like.objects.create(user=user,art=art)
                like_instance.save()
                liked = True
            like_count = art.artwork_likes.count()
            return JsonResponse({'liked':liked,'like_count':like_count,'art_pk':art_pk})

class ArtDetailView(View):
    def get(self, request, *args, **kwargs):
        user = request.user.userprofile
        art = Artwork.objects.get(pk=self.kwargs.get('pk'))
        liked = False
        color = ""
        if art.artwork_likes.filter(id=user.id).exists():
            liked = True
            color = "text-danger"
        context = {
        'object': art,
        'color':color,
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
