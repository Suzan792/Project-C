from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from art.models import Artwork

def index(request):
    Artwork_list = Artwork.objects.all()
    paginator = Paginator(Artwork_list, 6)
    page = request.GET.get('page')
    Artworks = paginator.get_page(page)
    return render(request,'index.html',{'Artworks':Artworks})
def contact_page(request):
    return render(request,'contact.html')
