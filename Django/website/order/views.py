from django.shortcuts import render, get_list_or_404
from django.views.generic import View

from .models import OrderHistory

# Create your views here.

def return_orders(request):
    orders = []
    order_list = []
    order_items = []

    try:
        order_items = get_list_or_404(OrderHistory.objects.order_by('-id'), user=request.user)
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