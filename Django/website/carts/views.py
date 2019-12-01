from django.shortcuts import render, HttpResponseRedirect
from .models import Cart
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