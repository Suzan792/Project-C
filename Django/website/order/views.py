from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import View

from .models import OrderHistoryItem
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.models import ST_PP_COMPLETED

def add_orders(request, order, order_date, order_datetime):
    '''
    This function is used to add orders to the order history.
    '''
    design = order
    product = design.product
    artwork = design.art

    order_history_item_instance = OrderHistoryItem.objects.create(
        name = artwork.artwork_name + '   |   ' + product.product_name,
        design_photo=design.design_photo,
        user=request.user,
        order_date=order_date,
        order_datetime=order_datetime,
        status='NP',  
        paid_price=artwork.artwork_price + product.price,
        quantity=1,   
    )
    
    return order_history_item_instance

def get_orders(request):
    '''
    This function returns orders for the order history.
    '''
    orders = []
    order_list = []
    order_items = []

    try:
        order_items = get_list_or_404(OrderHistoryItem.objects.order_by('-id'), user=request.user)
        old_item = None
        for item in order_items:
            check_status(request, item)

            if old_item == None:
                old_item = item
            
            if old_item.order_datetime != item.order_datetime:
                orders.append(order_list)
                order_list = []
             
            order_list.append(item)
          
            old_item = item
        orders.append(order_list)
    except:
        print('No orders')

    template = 'orders/my_orders.html'
    context = { 'orders' : orders, 'amount_of_orders' : len(order_items) }

    return render(request, template, context)

def check_status(request, item):
    '''
    This function checks if items with the status 'NP' (Not paid) have the status 'Completed'.
    If they do, the item's status is changed to 'IM' (In the making).
    If they don't, nothing changes.
    One item can be checked at a time.
    '''
    if item.status == 'NP':
        try:
            paypal_ipn = get_object_or_404(PayPalIPN.objects, invoice = str(item.order_datetime)[:26])
            if paypal_ipn.payment_status == ST_PP_COMPLETED:
                item.status = 'IM'
                item.save()
            print('Found IPN')
        except:
            print('No IPN')
