from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from art.models import Artwork


def contact_page(request):
    return render(request,'contact.html')
class ArtListView(ListView):
    model = Artwork
    template_name = 'index.html'
    context_object_name = 'Artworks'
    ordering = ['-upload_date']
    paginate_by = 6
    queryset = Artwork.objects.all()

class ArtDetailView(DetailView):
    model = Artwork
