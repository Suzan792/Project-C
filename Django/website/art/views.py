from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, DeleteView, UpdateView
from art.forms import CommentForm
from art.models import Artwork, Comment
from products.models import Design, Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import forms


# Create your views here.


class artistworkListView(ListView):
    model = Artwork
    template_name = 'artistwork.html'


@login_required
def upload_art(request):
    if request.method == 'POST':
        form = forms.uploadArt(request.POST, request.FILES)
        if form.is_valid():
            # save to db
            instance = form.save(commit=False)
            instance.artist = request.user.userprofile
            instance.save()
            messages.success(request, f'Your ArtWork  is uploaded')
            return redirect('artDetail_page', form.instance.id)
    else:
        form = forms.uploadArt()
    return render(request, 'uploadArt.html', {'form': form})


class ArtworkUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Artwork
    fields = ['artwork_name', 'artwork_description', 'artwork_photo']
    template_name = 'uploadArt.html'
    success_url = '/artistwork'

    def form_valid(self, form):
        form.instance.artist = self.request.user.userprofile
        return super().form_valid(form)

    # check of current user is the owner of this artwork
    def test_func(self):
        Artwork = self.get_object()
        if self.request.user == Artwork.artist.user:
            print(self.request.user)
            return True
        return False


class deleteArtView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Artwork
    success_url = '/'

    # check of current user is the owner of this artwork
    def test_func(self):
        Artwork = self.get_object()
        if self.request.user == Artwork.artist.user:
            return True
        return False


class ArtDetailView(View):
    def get(self, request, *args, **kwargs):
        art = Artwork.objects.get(pk=self.kwargs.get('pk'))
        designs = Design.objects.filter(art=art, user=None)
        products = Product.objects.all()
        productWithoutDesign = []
        for product in products:
            i = products.count()
            for design in designs:
                if product == design.product:
                    i=i-1
            if i==products.count():
                productWithoutDesign.append(product)



        comments = Comment.objects.filter(artwork=art).order_by('-id')
        comment_form = CommentForm()
        liked = False
        if request.user.is_authenticated:
            user = request.user.userprofile
            if art.artwork_likes.filter(id=user.id).exists():
                liked = True
        context = {
            'object': art,
            'designs': designs,
            'products': productWithoutDesign,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(request, 'art/artwork_detail.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and 'commentForm' in request.POST:
            art = Artwork.objects.get(pk=self.kwargs.get('pk'))
            designs = Design.objects.filter(art=art, user=None)
            comments = Comment.objects.filter(artwork=art).order_by('-id')
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = Comment.objects.create(artwork=art, commenter=request.user.userprofile,
                                                 comment=request.POST.get('comment'))
                comment.save()
                return redirect('artDetail_page', art.id)
            context = {
                'object': art,
                'designs': designs,
                'comments': comments,
                'comment_form': comment_form,
            }
            return render(request, 'art/artwork_detail.html', context)
        if request.user.is_authenticated:
            art = Artwork.objects.get(pk=self.kwargs.get('pk'))
            user = request.user.userprofile
            if art.artwork_likes.filter(id=user.id).exists():
                art.artwork_likes.remove(user)
                liked = False
            else:
                art.artwork_likes.add(user)
                liked = True
            art_pk = self.kwargs.get('pk')
            like_count = art.artwork_likes.count()
            return JsonResponse({'liked':liked,'like_count':like_count,'art_pk':art_pk})
