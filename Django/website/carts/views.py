from datetime import datetime
from paypal.standard.forms import PayPalPaymentsForm

from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Cart
from products.models import Product, Design
from django.views.generic import View
from django.urls import reverse


# from product.models import Product

def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
    else:
        empty_message = "Your Cart is Empty, please add something to your cart."
        context = {"empty": True, "empty_message": empty_message}

    try:
        the_id
    except cart.DoesNotExist:
        pass
    if the_id:
        new_total = 0.00
        for a in cart.item.all():
            new_total += float(a.product.price + a.art.artwork_price)
        request.session['items_total'] = cart.item.count()
        cart.total = round(new_total, 2)
        cart.save()

        payment_data = payment(request, cart, new_total)
        order = payment_data[0]
        form = payment_data[1]

        context = {"cart": cart, 'order': order, 'form': form}

    template = "carts/view.html"
    return render(request, template, context)


class FreshCart(View):
    def get(self, request, *args, **kwargs):
        request.session.set_expiry(12000)
        try:
            the_id = request.session['cart_id']
        except:
            new_cart = Cart()
            new_cart.save()
            request.session['cart_id'] = new_cart.id
            the_id = new_cart.id

        cart = Cart.objects.get(id=the_id)

        try:
            product = Design.objects.get(id=self.kwargs.get('design_pk'))
        except Product.DoesNotExist:
            pass
        except:
            pass
        if not product in cart.item.all():
            cart.item.add(product)
        else:
            cart.item.remove(product)
        return HttpResponseRedirect(reverse("cart"))


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
