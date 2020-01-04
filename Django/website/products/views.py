from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from products.models import Design, Product, DesignArtCoordinate, DesignArtFrameCoordinate, DesignTextCoordinate
from art.models import Artwork
from django.utils import timezone
from django.urls import reverse
from . import forms
from . import services
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
import os
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
            text = design.designTextCoordinate.text
            text_top = design.designTextCoordinate.coordinate_top
            text_left = design.designTextCoordinate.coordinate_left
            font_color = design.designTextCoordinate.font_color
            font_weight = design.designTextCoordinate.font_weight
            font = design.designTextCoordinate.font
            font_style = design.designTextCoordinate.font_style
            font_size =design.designTextCoordinate.font_size

            status = 'success'
            return JsonResponse({'status':status,'top':top,'left':left,'height':height, 'width':width, 'rotation':rotation, 'frame_top': frame_top,
            'frame_left': frame_left, 'frame_height': frame_height, 'frame_width': frame_width, 'frame_border_radius':frame_border_radius,'id':id,'text':text,
            'text_top':text_top,'text_left':text_left,'font_color':font_color,'font_weight':font_weight,'font':font,'font_style':font_style,'font_size':font_size})

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
            designs = Design.objects.filter(art= art, product= product, user__isnull=True,)
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
                services.deleteDesign(request.POST['pk'])
                return JsonResponse({})
            if request.POST.get('action')== "save":
                imageData = request.POST.get('image')
                design = Design.objects.get(id= request.POST.get('designId'))

                ##art
                art_top =  request.POST.get('top')[:-2]
                art_left =  request.POST.get('left')[:-2]
                art_height = request.POST.get('height')[:-2]
                art_width = design.designArtCoordinate.width = request.POST.get('width')[:-2]
                ##artframe
                frame_rotation = request.POST.get('rotation')
                frame_top  = request.POST.get('frame_top')[:-2]
                frame_left = request.POST.get('frame_left')[:-2]
                frame_width = request.POST.get('frame_width')[:-2]
                frame_height = request.POST.get('frame_height')[:-2]
                frame_border_radius = request.POST.get('frame_border_radius')[:-2]
                ##text
                text_font = request.POST.get('font')
                text_weight = request.POST.get('font_weight')
                text_style = request.POST.get('font_style')
                text_top = request.POST.get('text_top')[:-2]
                text_left = request.POST.get('text_left')[:-2]
                text_color = request.POST.get('font_color')
                text = request.POST.get('text')
                text_size = request.POST.get('text_size')[:-2]

                services.saveDesignCoordinate(
                    design = design,imageData=imageData,
                    art_top=art_top,art_left=art_left,art_height=art_height,art_width=art_width,frame_top=frame_top
                    ,frame_left=frame_left,frame_width=frame_width,frame_height=frame_height,frame_border_radius=frame_border_radius,
                    frame_rotation=frame_rotation,text_font=text_font,text_top=text_top,text_left=text_left,text_weight=text_weight
                    ,text_style=text_style,text_color=text_color,text_size=text_size,text=text)
                return JsonResponse({'status':"success"})
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
                    text = design.designTextCoordinate.text
                    text_top = design.designTextCoordinate.coordinate_top
                    text_left = design.designTextCoordinate.coordinate_left
                    font_color = design.designTextCoordinate.font_color
                    font_weight = design.designTextCoordinate.font_weight
                    font = design.designTextCoordinate.font
                    font_style = design.designTextCoordinate.font_style
                    font_size =design.designTextCoordinate.font_size

                    status = 'success'
                    return JsonResponse({'status':status,'top':top,'left':left,'height':height, 'width':width, 'rotation':rotation, 'frame_top': frame_top,
                    'frame_left': frame_left, 'frame_height': frame_height, 'frame_width': frame_width, 'frame_border_radius':frame_border_radius,'id':id,'text':text,
                    'text_top':text_top,'text_left':text_left,'font_color':font_color,'font_weight':font_weight,'font':font,'font_style':font_style,'font_size':font_size})
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
                services.deleteDesign(request.POST['pk'])
                return JsonResponse({'status':"success"})
            if request.POST.get('action')== "save":
                imageData = request.POST.get('image')
                design = Design.objects.get(id= request.POST.get('designId'))
                ##art
                art_top =  request.POST.get('top')[:-2]
                art_left =  request.POST.get('left')[:-2]
                art_height = request.POST.get('height')[:-2]
                art_width = design.designArtCoordinate.width = request.POST.get('width')[:-2]
                ##artframe
                frame_rotation = request.POST.get('rotation')
                frame_top  = request.POST.get('frame_top')[:-2]
                frame_left = request.POST.get('frame_left')[:-2]
                frame_width = request.POST.get('frame_width')[:-2]
                frame_height = request.POST.get('frame_height')[:-2]
                frame_border_radius = request.POST.get('frame_border_radius')[:-2]
                ##text
                text_font = request.POST.get('font')
                text_weight = request.POST.get('font_weight')
                text_style = request.POST.get('font_style')
                text_top = request.POST.get('text_top')[:-2]
                text_left = request.POST.get('text_left')[:-2]
                text_color = request.POST.get('font_color')
                text = request.POST.get('text')
                text_size = request.POST.get('text_size')[:-2]

                services.saveDesignCoordinate(
                    design = design, imageData= imageData,
                    art_top=art_top,art_left=art_left,art_height=art_height,art_width=art_width,frame_top=frame_top
                    ,frame_left=frame_left,frame_width=frame_width,frame_height=frame_height,frame_border_radius=frame_border_radius,
                    frame_rotation=frame_rotation,text_font=text_font,text_top=text_top,text_left=text_left,text_weight=text_weight
                    ,text_style=text_style,text_color=text_color,text_size=text_size,text=text)
                return JsonResponse({'status':'success'})
        else:
            art_pk = self.kwargs.get('art_pk')
            product_pk = request.POST.get('product')
            form = forms.CreateProductDesignForm(request.POST)
            if form.is_valid():
                form.ArtistSave(art_pk,product_pk)
            return HttpResponseRedirect(reverse('editProduct_page',args=[art_pk]))
