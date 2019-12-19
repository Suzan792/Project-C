from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from products.models import Design, Product, DesignArtCoordinate, DesignArtFrameCoordinate, DesignTextCoordinate
from art.models import Artwork
from django.utils import timezone
from django.urls import reverse
from . import forms
from django.http import JsonResponse, HttpResponse
from django.db.models import Q

# Create your views here.
class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        art = Artwork.objects.get(id = self.kwargs.get('art_pk'))
        product = Product.objects.get(id = self.kwargs.get('product_pk'))
        if request.is_ajax():
            design = Design.objects.get(id= request.GET.get('designId'))
            id = request.GET.get('designId')
            top = design.designArtCoordinate.coordinate_top
            left = design.designArtCoordinate.coordinate_left
            height = design.designArtCoordinate.height
            width = design.designArtCoordinate.width
            frame_top = design.designArtFrameCoordinate.frame_coordinate_top
            frame_left =design.designArtFrameCoordinate.frame_coordinate_left
            frame_height = design.designArtFrameCoordinate.frame_height
            frame_width = design.designArtFrameCoordinate.frame_width
            rotation = design.designArtFrameCoordinate.rotation
            frame_border_radius = design.designArtFrameCoordinate.frame_border_radius
            status = 'success'
            return JsonResponse({'status':status,'top':top,'left':left,'height':height, 'width':width, 'rotation':rotation, 'frame_top': frame_top,
            'frame_left': frame_left, 'frame_height': frame_height, 'frame_width': frame_width, 'frame_border_radius':frame_border_radius,'id':id})
        elif request.user.is_authenticated:
            user = request.user.userprofile
            designs = Design.objects.filter(Q(art=art), Q(product=product), Q(user=user) | Q(user=None)).order_by('-user')
            form = forms.CreateProductDesignForm()
            context = {
            'art':art,
            'designs':designs,
            'product':product,
            'form':form,
            }
            return render(request, 'products/product_detail.html', context)
        else:
            art = Artwork.objects.get(id = self.kwargs.get('art_pk'))
            product = Product.objects.get(id = self.kwargs.get('product_pk'))
            designArtCoordinate = Product.objects.create()
            designArtFrameCoordinate = Product.objects.create()
            designTextCoordinate = Product.objects.create()
            designs = Design.objects.filter(art= art, product= product, user__isnull=True,
            designArtCoordinate =designArtCoordinate,designArtFrameCoordinate=designArtFrameCoordinate,designTextCoordinate=designTextCoordinate)
            form = forms.CreateProductDesignForm()
            context = {
            'art':art,
            'designs':designs,
            'product':product,
            'form':form,
            }
            return render(request, 'products/product_detail.html', context)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            if request.POST.get('action')== "delete":
                Design.objects.get(id= request.POST['pk']).delete()
                return JsonResponse({'status':"success"})
            else:
                design = Design.objects.get(id= request.POST.get('designId'))
                ##art
                design.designArtCoordinate.coordinate_top = request.POST.get('top')[:-2]
                design.designArtCoordinate.coordinate_left = request.POST.get('left')[:-2]
                design.designArtCoordinate.height = request.POST.get('height')[:-2]
                design.designArtCoordinate.width = request.POST.get('width')[:-2]
                ##artframe
                design.designArtFrameCoordinate.rotation = str(request.POST.get('rotation'))
                design.designArtFrameCoordinate.frame_coordinate_top = request.POST.get('frame_top')[:-2]
                design.designArtFrameCoordinate.frame_coordinate_left = request.POST.get('frame_left')[:-2]
                design.designArtFrameCoordinate.frame_width = request.POST.get('frame_width')[:-2]
                design.designArtFrameCoordinate.frame_height = request.POST.get('frame_height')[:-2]
                design.designArtFrameCoordinate.frame_border_radius = request.POST.get('frame_border_radius')[:-2]
                ##text
                design.designTextCoordinate.font = request.POST.get('font')
                design.designTextCoordinate.font_weight = request.POST.get('font_weight')
                design.designTextCoordinate.font_style = request.POST.get('font_style')
                design.designTextCoordinate.coordinate_top = request.POST.get('text_top')[:-2]
                design.designTextCoordinate.coordinate_left = request.POST.get('text_left')[:-2]
                design.designTextCoordinate.font_color = request.POST.get('font_color')
                design.designTextCoordinate.text = request.POST.get('text')
                design.designTextCoordinate.font_size = request.POST.get('text_size')[:-2]

                design.designArtCoordinate.save()
                design.designArtFrameCoordinate.save()
                design.designTextCoordinate.save()
                return JsonResponse({'status':'success'})
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
                    id = request.GET.get('designId')
                    top = design.designArtCoordinate.coordinate_top
                    left = design.designArtCoordinate.coordinate_left
                    height = design.designArtCoordinate.height
                    width = design.designArtCoordinate.width
                    frame_top = design.designArtFrameCoordinate.frame_coordinate_top
                    frame_left =design.designArtFrameCoordinate.frame_coordinate_left
                    frame_height = design.designArtFrameCoordinate.frame_height
                    frame_width = design.designArtFrameCoordinate.frame_width
                    rotation = design.designArtFrameCoordinate.rotation
                    frame_border_radius = design.designArtFrameCoordinate.frame_border_radius
                    status = 'success'
                    return JsonResponse({'status':status,'top':top,'left':left,'height':height, 'width':width, 'rotation':rotation, 'frame_top': frame_top,
                    'frame_left': frame_left, 'frame_height': frame_height, 'frame_width': frame_width, 'frame_border_radius':frame_border_radius,'id':id})
                else:
                    form = forms.CreateProductDesignForm()
                    designs = Design.objects.filter(art=art,user=None).order_by('-created_on')
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
            if request.POST.get('action')== "delete":
                Design.objects.get(id= request.POST['pk']).delete()
                return JsonResponse({'status':"success"})
            else:
                design = Design.objects.get(id= request.POST.get('designId'))
                design.designArtCoordinate.coordinate_top = request.POST.get('top')[:-2]
                design.designArtCoordinate.coordinate_left = request.POST.get('left')[:-2]
                design.designArtCoordinate.height = request.POST.get('height')[:-2]
                design.designArtCoordinate.width = request.POST.get('width')[:-2]
                design.designArtFrameCoordinate.rotation = str(request.POST.get('rotation'))
                design.designArtFrameCoordinate.frame_coordinate_top = request.POST.get('frame_top')[:-2]
                design.designArtFrameCoordinate.frame_coordinate_left = request.POST.get('frame_left')[:-2]
                design.designArtFrameCoordinate.frame_width = request.POST.get('frame_width')[:-2]
                design.designArtFrameCoordinate.frame_height = request.POST.get('frame_height')[:-2]
                design.designArtFrameCoordinate.frame_border_radius = request.POST.get('frame_border_radius')[:-2]
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
