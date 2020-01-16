from django.shortcuts import render
from django.views.generic import ListView
from art.models import Artwork
from django.db.models import Q, Count


class SearchResultsView(ListView):
    model = Artwork
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.kwargs.get('query')
        order = '-upload_date_time'
        category_ = self.kwargs.get('category')
        if self.kwargs.get('filter')== None :
            return Artwork.objects.filter(Q(artwork_name__icontains=query)).order_by(order)
        if self.kwargs.get('filter')=='newest':
            order = '-upload_date_time'
        if self.kwargs.get('filter')=='oldest':
            order = 'upload_date_time'
        if self.kwargs.get('filter')=='highestPrice':
            order = '-artwork_price'
        if self.kwargs.get('filter')=='lowestPrice':
            order = 'artwork_price'
        if self.kwargs.get('filter')=='mostLiked':
            return  Artwork.objects.filter(Q(artwork_name__icontains=query)).annotate(Count('artwork_likes')).order_by('-artwork_likes__count')

        if category_=='all':
            return Artwork.objects.filter(Q(artwork_name__icontains=query)).order_by(order)

        return Artwork.objects.filter(Q(artwork_name__icontains=query),Q(category=category_)).order_by(order)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['filter'] = self.kwargs.get('filter')
        context['category'] = self.kwargs.get('category')
        context['query'] = self.kwargs.get('query')
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
