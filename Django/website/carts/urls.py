from django.urls import include, path

from . import views

urlpatterns = [
    path('cart/', views.get_shopping_cart, name='cart'),
    path('cart/<int:design_pk>/', views.add_delete_product, name='update_cart'),
    path('cart/request_to_paypal/', views.request_to_paypal, name='request_to_paypal'),
    path('payment/<int:product_pk>/<int:art_pk>/', views.payment, name='payment'),
    path('payment_done', views.payment_done, name='payment_done'),
    path('payment_cancelled', views.payment_cancelled, name='payment_cancelled'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('wish-list/', views.get_wishlist, name='wishlist_page'),
    path('wish-list/<int:design_pk>/', views.add_wish_item, name='add_to_wishlist'),
    path('wish-list/delete/<int:design_pk>/', views.delete_wish_item, name='delete_from_wishlist'),
]
