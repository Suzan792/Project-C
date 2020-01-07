from datetime import datetime
from paypal.standard.conf import POSTBACK_ENDPOINT, SANDBOX_POSTBACK_ENDPOINT
import requests

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .models import Cart
from .forms import PayPalForm
from order import views as order_views 
from products.models import Product, Design

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
    '''
    This function returns the cart and the PayPal form (that will be sent to PayPal).
    You need to pass request, a cart and the total paid price for an order as parameters.
    '''
    host = request.get_host()

    paypal_form = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': total,
        'item_name': 'Order {}'.format(datetime.today()),
        'invoice': '',
        'currency_code': 'EUR',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
    }

    form = PayPalForm(initial=paypal_form)

    return cart, form


@csrf_exempt
def payment_done(request):
    messages.success(request, f'Payment succesful')
    return redirect('home_page')

@csrf_exempt
def payment_cancelled(request):
    messages.warning(request, f'Payment was cancelled')
    return redirect('cart')

def move_to_orderhistory(request, cart):
    '''
    Use this function to add an item to the order history.
    It returns the date and time of the order so it can be passed as an invoice to paypal.
    '''
    today = datetime.today()
    date_time = datetime.now()

    for item in cart.item.all():
        order_views.add_orders(request, item, today, date_time)
        cart.item.remove(item)

    return date_time

@csrf_exempt
def request_to_paypal(request):
    '''
    This view calls a function that moves the products in the cart to the order history.
    It also sends a post request to PayPal.
    '''
    def get_cart(request):
        '''
        This function returns the current cart if its id is saved in the session. 
        '''
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        return cart

    date_time = move_to_orderhistory(request, get_cart(request))

    post_data = {
        'cmd' : request.POST.get("cmd",''),
        'charset' : request.POST.get("charset",''),
        'currency_code' : request.POST.get("currency_code",''),
        'no_shipping' : request.POST.get("no_shipping",''),
        'business' : request.POST.get("business",''),
        'amount' : request.POST.get("amount",''),
        'item_name' : request.POST.get("item_name",''),
        'invoice' : date_time,
        'notify_url' : request.POST.get("notify_url",''),
        'cancel_return' : request.POST.get("cancel_return",''),
        'return' : request.POST.get("return",''),
    }

    def get_endpoint():
        '''
        Returns the endpoint url for the form. 
        This is where the information in the form will be sent.
        '''
        if getattr(settings, 'PAYPAL_TEST', True):
            return SANDBOX_POSTBACK_ENDPOINT
        else:
            return POSTBACK_ENDPOINT
        
    r = requests.post(get_endpoint(), data=post_data)

    return redirect(r.url)
    
