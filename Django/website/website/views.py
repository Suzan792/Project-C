from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View
from art.models import Artwork
from like_count.models import Like
from django.utils import timezone


def contact_page(request):
    return render(request,'contact.html')
class ArtListView(ListView):
    model = Artwork
    template_name = 'index.html'
    context_object_name = 'Artworks'
    ordering = ['-upload_date']
    paginate_by = 6


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user.userprofile
            context['liked_list'] = Like.objects.filter(user=user)
        return context

class ArtDetailView(View):
    def get(self, request, *args, **kwargs):
        user = request.user.userprofile
        object = Artwork.objects.get(pk=self.kwargs.get('pk'))
        liked = False
        if Like.objects.filter(user=user).filter(art=object):
            liked = True
        context = {
        'object': object,
        'liked':liked,
        }
        return render(request, 'art/artwork_detail.html', context)
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            art = Artwork.objects.get(pk=self.kwargs.get('pk'))
            user = request.user.userprofile
            if Like.objects.filter(user=user).filter(art=art):
                Like.objects.filter(user=user).filter(art=art).delete()
                liked = False
            else:
                like_instance = Like.objects.create(user=user,art=art)
                like_instance.save()
                liked = True
            context = {
                'object': art,
                'liked':liked,
                }
            return render(request,'art/artwork_detail.html',context)
