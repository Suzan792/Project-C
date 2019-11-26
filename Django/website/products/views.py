from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.views.generic import View
from products.models import Product, Design
from art.models import Artwork
from django.utils import timezone
import json
from django.urls import reverse
from . import forms
from django.http import JsonResponse
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from .models import Order
from django.views.decorators.csrf import csrf_exempt

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
            width = design.width
            frame_top = design.frame_coordinate_top
            frame_left =design.frame_coordinate_left
            frame_height = design.frame_height
            frame_width = design.frame_width
            rotation = design.rotation
            status = 'success'
            return JsonResponse({'status':status,'top':top,'left':left,'height':height, 'width':width, 'rotation':rotation, 'frame_top': frame_top,
            'frame_left': frame_left, 'frame_height': frame_height, 'frame_width': frame_width})
        else:
            designs = Design.objects.filter(art=art).order_by('product')
            context = {
            'art':art,
            'designs': designs,
            'form':form
            }
            return render(request, 'products/product_design_edit.html', context)
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            art_id = request.POST.get('artId')
            product_id = request.POST.get('productId')
            art = Artwork.objects.get(pk=art_id)
            product = Product.objects.get(pk=product_id)
            design = Design.objects.get(art=art,product=product)
            design.coordinate_top = request.POST.get('top')[:-2]
            design.coordinate_left = request.POST.get('left')[:-2]
            design.height = request.POST.get('height')[:-2]
            design.width = request.POST.get('width')[:-2]
            design.rotation = str(request.POST.get('rotation'))
            design.frame_coordinate_top = request.POST.get('frame_top')[:-2]
            design.frame_coordinate_left = request.POST.get('frame_left')[:-2]
            design.frame_width = request.POST.get('frame_width')[:-2]
            design.frame_height = request.POST.get('frame_height')[:-2]
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
class PaymentView(View):
    def payment(self, request):
        # order_id = request.session.get('order_id')
        # order = get_object_or_404(Order, id=order_id)
        product_id = request.session.get('product_id')
        order = get_object_or_404(Product, id=product_id)
        host = request.get_host()
    
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': '%.2f' % order.total_cost().quantize(Decimal('.01')),
            'item_name': 'Order {}'.format(order.id),
            'invoice': str(order.id),
            'currency_code': 'EUR',
            'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
            'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
        }
    
        form = PayPalPaymentsForm(initial=paypal_dict)
        return render(request, 'products/templates/payment/payment.html', {'order': order, 'form': form})

    @csrf_exempt
    def payment_done(self, request):
        return render(request, 'products/templates/payment/payment_done.html')

    @csrf_exempt
    def payment_canceled(self, request):
        return render(request, 'products/templates/payment/payment_cancelled.html')
