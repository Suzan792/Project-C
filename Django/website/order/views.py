from django.shortcuts import render, get_list_or_404
from django.views.generic import View

from .models import OrderHistory

# Create your views here.

def return_orders(request):
    template = 'orders/my_orders.html'
    # context
    print(request.user)

    orders = []
    try:
        orders = get_list_or_404(OrderHistory, user=request.user)
    except:
        print('No orders')

    amount_of_orders = len(orders)
    return render(request, template, { 'orders' : orders, 'amount_of_orders' : amount_of_orders })