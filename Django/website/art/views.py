from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, View , DeleteView
from art.models import Artwork
from products.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import forms
from users.models import User,UserProfile
from django.contrib.auth.models import User

# Create your views here.

class artistworkListView(ListView):
    model = Artwork
    template_name = 'artistwork.html'


@login_required
def upload_art(request):
    if request.method == 'POST':
        form = forms.uploadArt(request.POST,request.FILES)
        if form.is_valid():
            # save to db
            instance = form.save(commit=False)
            instance.artist = request.user.userprofile
            instance.save()
            messages.success(request, f'Your ArtWork  is uploaded')
            return redirect('artDetail_page',form.instance.id)
    else:
        form = forms.uploadArt()
    return render(request,'uploadArt.html',{'form':form})

class deleteArtView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Artwork
    success_url = '/'

    def test_func(self):
        Artwork = self.get_object()
        print(self.request.user)
        print(Artwork.artist)
        if self.request.user == Artwork.artist.user:
            print(self.request.user)
            return True
        return False

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
