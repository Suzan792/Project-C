from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from products.models import Design, Product
from art.models import Artwork
from django.utils import timezone
from django.urls import reverse
from . import forms
from django.http import JsonResponse, HttpResponse

# Create your views here.
class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        art = Artwork.objects.get(id = self.kwargs.get('art_pk'))
        product = Product.objects.get(id = self.kwargs.get('product_pk'))
        designs = Design.objects.filter(art= art, product= product)
        form = forms.CreateProductDesignForm()
        context = {
        'designs':designs,
        'form':form,
        }
        return render(request, 'products/product_detail.html', context)
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            print("---------------------------------------------------"+request.POST.get('designId'))
            print(request.POST.get('designId'))
            design = Design.objects.get(id= request.POST.get('designId'))
            design.coordinate_top = request.POST.get('top')[:-2]
            design.coordinate_left = request.POST.get('left')[:-2]
            design.height = request.POST.get('height')[:-2]
            design.width = request.POST.get('width')[:-2]
            design.rotation = str(request.POST.get('rotation'))
            design.frame_coordinate_top = request.POST.get('frame_top')[:-2]
            design.frame_coordinate_left = request.POST.get('frame_left')[:-2]
            design.frame_width = request.POST.get('frame_width')[:-2]
            design.frame_height = request.POST.get('frame_height')[:-2]
            design.frame_border_radius = request.POST.get('frame_border_radius')[:-2]
            design.save()
            status = 'success'
            return JsonResponse({'status':status})
        if request.POST.get("add_design"):
            art_pk = self.kwargs.get('art_pk')
            product_pk =  self.kwargs.get('product_pk')
            user_pk = request.user.id
            form = forms.CreateProductDesignForm()
            form.UserSave(art_pk,product_pk,user_pk)
            return HttpResponseRedirect(reverse('productDetail_page',kwargs={'art_pk': art_pk,'product_pk':product_pk}))


class ProductDesignEditView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            art = Artwork.objects.get(pk=self.kwargs.get('art_pk'))
            if request.user.userprofile.id == art.artist.id:
                if request.is_ajax():
                    design = Design.objects.get(id= request.GET.get('designId'))
                    top = design.coordinate_top
                    left = design.coordinate_left
                    height = design.height
                    width = design.width
                    frame_top = design.frame_coordinate_top
                    frame_left =design.frame_coordinate_left
                    frame_height = design.frame_height
                    frame_width = design.frame_width
                    rotation = design.rotation
                    frame_border_radius = design.frame_border_radius
                    status = 'success'
                    return JsonResponse({'status':status,'top':top,'left':left,'height':height, 'width':width, 'rotation':rotation, 'frame_top': frame_top,
                    'frame_left': frame_left, 'frame_height': frame_height, 'frame_width': frame_width, 'frame_border_radius':frame_border_radius})
                else:
                    form = forms.CreateProductDesignForm()
                    designs = Design.objects.filter(art=art).order_by('product')
                    context = {
                    'art':art,
                    'designs': designs,
                    'form':form
                    }
                    return render(request, 'products/product_design_edit.html', context)
            else:
                return HttpResponse("This artwork doesn't belong to you.")
        else:
            return HttpResponse("You must be logged in to access this page")


    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            print("---------------------------------------------------"+request.POST.get('designId'))
            print(request.POST.get('designId'))
            design = Design.objects.get(id= request.POST.get('designId'))
            design.coordinate_top = request.POST.get('top')[:-2]
            design.coordinate_left = request.POST.get('left')[:-2]
            design.height = request.POST.get('height')[:-2]
            design.width = request.POST.get('width')[:-2]
            design.rotation = str(request.POST.get('rotation'))
            design.frame_coordinate_top = request.POST.get('frame_top')[:-2]
            design.frame_coordinate_left = request.POST.get('frame_left')[:-2]
            design.frame_width = request.POST.get('frame_width')[:-2]
            design.frame_height = request.POST.get('frame_height')[:-2]
            design.frame_border_radius = request.POST.get('frame_border_radius')[:-2]
            design.save()
            status = 'success'
            return JsonResponse({'status':status})
        else:
            art_pk = self.kwargs.get('art_pk')
            product_pk = request.POST.get('product')
            form = forms.CreateProductDesignForm(request.POST)
            if form.is_valid():
                form.ArtistSave(art_pk,product_pk)
            return HttpResponseRedirect(reverse('editProduct_page',args=[art_pk]))
