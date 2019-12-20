from django.shortcuts import render, get_list_or_404
from django.views.generic import View

from .models import OrderHistory, OrderProduct, OrderArtwork, OrderDesign

# Create your views here.

def add_orders(request, order, order_date, order_datetime):
    '''
    This function is used to add orders to the order history.
    '''
    design = order
    product = design.product
    artwork = design.art

    order_product_instance = OrderProduct.objects.create(
        product_name=product.product_name,
        product_photo=product.product_photo,
        price=product.price,
    )
    order_artwork_instance = OrderArtwork.objects.create(
        artwork_name=artwork.artwork_name,
        artwork_photo=artwork.artwork_photo,
        artwork_price=artwork.artwork_price,
    )
    order_design_instance = OrderDesign.objects.create(
        paid_price=order_artwork_instance.artwork_price + order_product_instance.price,
        quantity=1,
        product=order_product_instance,
        art=order_artwork_instance,
        coordinate_left=design.designArtCoordinate.coordinate_left,
        coordinate_top=design.designArtCoordinate.coordinate_top,
        height=design.designArtCoordinate.height,
        width=design.designArtCoordinate.width,
        frame_height=design.designArtFrameCoordinate.frame_height,
        frame_width=design.designArtFrameCoordinate.frame_width,
        frame_coordinate_left=design.designArtFrameCoordinate.frame_coordinate_left,
        frame_coordinate_top=design.designArtFrameCoordinate.frame_coordinate_top,
        frame_border_radius=design.designArtFrameCoordinate.frame_border_radius,
        rotation=design.designArtFrameCoordinate.rotation,
        text_coordinate_left = design.designTextCoordinate.coordinate_left,
        text_coordinate_top = design.designTextCoordinate.coordinate_top,
        text_font = design.designTextCoordinate.font,
        text_font_weight = design.designTextCoordinate.font_weight,
        text_font_style = design.designTextCoordinate.font_style,
        text_font_color = design.designTextCoordinate.font_color,
        text_font_size = design.designTextCoordinate.font_size,
        text = design.designTextCoordinate.text,
    )
    order_history_instance = OrderHistory.objects.create(
        design=order_design_instance,
        user=request.user,
        order_date=order_date,
        order_datetime=order_datetime,
        status='NP',     
    )

    print('Orders have been added')
    
    return order_history_instance

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
