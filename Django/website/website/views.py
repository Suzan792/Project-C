from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View
from art.models import Artwork
from like_count.models import Like


def contact_page(request):
    return render(request,'contact.html')
class ArtListView(ListView):
    model = Artwork
    template_name = 'index.html'
    context_object_name = 'Artworks'
    ordering = ['-upload_date']
    paginate_by = 6
    queryset = Artwork.objects.all()

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
