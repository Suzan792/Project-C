from django.shortcuts import render
from django.views.generic import ListView
from art.models import Artwork
from django.db.models import Q


class SearchResultsView(ListView):
    model = Artwork
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Artwork.objects.filter(Q(artwork_name__icontains=query))
        return object_list

