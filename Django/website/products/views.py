from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from products.models import Product
from django.utils import timezone
import json
from django.http import JsonResponse

# Create your views here.
class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=self.kwargs.get('pk'))
        context = {
        'product': product,
        }
        return render(request, 'products/product_detail.html', context)
