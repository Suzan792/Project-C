from django.shortcuts import render, get_list_or_404
from django.views.generic import View

from .models import OrderHistoryItem

# Create your views here.

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

    # template = 'orders/my_orders.html'

    # return render(request, template)

def return_orders(request):
    '''
    This function returns orders for the order history.
    '''
    orders = []
    order_list = []
    order_items = []

    try:
        order_items = get_list_or_404(OrderHistoryItem.objects.order_by('-id'), user=request.user)
        old_item = None
        # for item in order_items[::-1]:
        for item in order_items:

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
