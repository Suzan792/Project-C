from datetime import datetime
from paypal.standard.conf import POSTBACK_ENDPOINT, SANDBOX_POSTBACK_ENDPOINT

from django.conf import settings

from .models import Cart, Wish
from order import views as order_views 

def get_cart(request):
    cart_id = request.session['cart_id']
    cart = Cart.objects.get(id=cart_id)
    return cart

def get_users_wishlist(request):
    '''
    This function returns the logged in user's Wish List or makes a new one if it does not exist.
    '''
    wishlist = None
    if request.user.is_authenticated:
        try:
            wishlist = Wish.objects.get(user=request.user)
        except:
            wishlist = Wish(user = request.user)
            wishlist.save()

    return wishlist

def get_endpoint():
    '''
    Returns the endpoint url for the form. 
    This is where the information in the form will be sent.
    '''
    if getattr(settings, 'PAYPAL_TEST', True):
        return SANDBOX_POSTBACK_ENDPOINT
    else:
        return POSTBACK_ENDPOINT
    
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

def check_address(request):
    '''
    This function checks if the logged in user has specified his/her address. 
    If the user has done that, it will return True, if not, it will return False.
    '''
    user_profile = request.user.userprofile
    if user_profile.street_name == user_profile.house_number == user_profile.addition == user_profile.postcode == user_profile.city == None:
        return False
    else:
        return True
