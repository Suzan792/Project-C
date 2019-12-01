from paypal.standard.forms import PayPalPaymentsForm

from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Cart
from products.models import Product
# from django.core.urlresolvers import reverse

# from product.models import Product

def view(request):
    cart = Cart.objects.all()[0]
    context = {"cart": cart}
    template = "carts/view.html"

    new_total = 0.00
    for item in cart.products.all():
        new_total += float(item.price)
    cart.total = new_total
    cart.save()

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
def payment(request, product_pk, art_pk):
    product = get_object_or_404(Product, id=product_pk)
    host = request.get_host()

    paypal_form = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': product.price,
        'item_name': 'Product {}'.format(product.product_name),
        'invoice': str(product_pk),
        'currency_code': 'EUR',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_form)
    return render(request, 'payment/payment.html', {'order': product, 'form': form})

@csrf_exempt
def payment_done(request):
    return render(request, 'payment/payment_done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/payment_cancelled.html')
