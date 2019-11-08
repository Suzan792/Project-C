from django.shortcuts import get_object_or_404, render
from art.models import Artwork

def index(request):
    Artworks = Artwork.objects.all()[:5]
    return render(request,'index.html',{'Artworks':Artworks})
def contact_page(request):
    return render(request,'contact.html')
