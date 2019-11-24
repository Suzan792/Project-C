from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from products.models import Product
from art.models import Artwork
from django.utils import timezone
import json
from django.http import JsonResponse

# Create your views here.
class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        product_pk = self.kwargs.get('product_pk')
        art_pk = self.kwargs.get('art_pk')
        product = Product.objects.get(pk=product_pk)
        art = Artwork.objects.get(pk=art_pk)
        context = {
        'product': product,
        'art':art
        }
        return render(request, 'products/product_detail.html', context)
