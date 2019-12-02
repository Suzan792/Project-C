from datetime import datetime
from paypal.standard.forms import PayPalPaymentsForm

from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Cart
from products.models import Product
# from django.core.urlresolvers import reverse

# from product.models import Product

def view(request):
    cart = Cart.objects.all()[0]
    template = "carts/view.html"

    new_total = 0.00
    for item in cart.products.all():
        new_total += float(item.price)
    cart.total = new_total
    cart.save()

    payment_data = payment(request, cart, new_total)
    order = payment_data[0]
    form = payment_data[1]

    context = {"cart": cart, 'order': order, 'form': form}

    return render(request, template, context)



# def add_to_cart(request, slug):
#     cart = Cart.objects.all()[0]
#     try:
#         product = Product.objects.get(slug=slug)
#     except Product.DoesNotExist:
#         pass
#     except:
#         pass
#     if not product in cart.products.all():
#         cart.products.add(product)
#     else:
#         cart.products.remove(product)
#     return HttpResponseRedirect(reverse("cart"))

def payment(request, cart, total):
    host = request.get_host()

    paypal_form = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': total,
        'item_name': 'Order {}'.format(datetime.now()),
        'invoice': str(total),
        'currency_code': 'EUR',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
    }

    pform = PayPalPaymentsForm(initial=paypal_form)
    return cart, pform

@csrf_exempt
def payment_done(request):
    messages.success(request, f'Payment succesful')
    return redirect('home_page')

@csrf_exempt
def payment_cancelled(request):
    messages.warning(request, f'Payment was cancelled')
    return redirect('cart')
