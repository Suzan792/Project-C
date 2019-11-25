from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.views.generic import View
from products.models import Product, Design
from art.models import Artwork
from django.utils import timezone
import json
from django.urls import reverse
from . import forms
from django.http import JsonResponse

# Create your views here.
class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        product_pk = self.kwargs.get('product_pk')
        art_pk = self.kwargs.get('art_pk')
        product = Product.objects.get(pk=product_pk)
        art = Artwork.objects.get(pk=art_pk)
        design = Design.objects.get(art=art,product=product)
        context = {
        'design':design,
        }
        return render(request, 'products/product_detail.html', context)

class ProductDesignEditView(View):
    def get(self, request, *args, **kwargs):
        form = forms.CreateProductDesignForm()
        art_pk = self.kwargs.get('art_pk')
        art = Artwork.objects.get(pk=art_pk)
        if request.is_ajax():
            product_id = request.GET.get('productId')
            product = Product.objects.get(pk=product_id)
            design = Design.objects.get(art=art,product=product)
            top = design.coordinate_top
            left =design.coordinate_left
            height = design.height
            status = 'success'
            print(status)
            return JsonResponse({'status':status,'top':top,'left':left,'height':height})
        else:
            designs = Design.objects.filter(art=art).order_by('product')
            context = {
            'art':art,
            'designs': designs,
            'form':form
            }
            return render(request, 'products/product_design_edit.html', context)
    def post(self, request, *args, **kwargs):
        print("hssi")
        if request.is_ajax():
            art_id = request.POST.get('artId')
            product_id = request.POST.get('productId')
            art = Artwork.objects.get(pk=art_id)
            product = Product.objects.get(pk=product_id)
            design = Design.objects.get(art=art,product=product)
            design.coordinate_top = request.POST.get('top')[:-2]
            design.coordinate_left = request.POST.get('left')[:-2]
            design.height = request.POST.get('height')[:-2]
            print(request.POST.get('left'))
            print(request.POST.get('top'))
            print(request.POST.get('height'))
            print("hi")
            design.save()
            status = 'success'
            return JsonResponse({'status':status})
        else:
            art_pk = self.kwargs.get('art_pk')
            product_pk = request.POST.get('product')
            form = forms.CreateProductDesignForm(request.POST)
            if form.is_valid():
                form.save(art_pk,product_pk)
            return HttpResponseRedirect(reverse('editProduct_page',args=[art_pk]))
