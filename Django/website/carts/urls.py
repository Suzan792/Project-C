from django.urls import include, path
from . import views
from .views import FreshCart


urlpatterns = [
    path('cart/', views.view, name='cart'),
    path('cart/<int:design_pk>/', FreshCart.as_view(), name='update_cart'),
    path('payment/<int:product_pk>/<int:art_pk>/', views.payment, name='payment'),
    path('payment_done', views.payment_done, name='payment_done'),
    path('payment_cancelled', views.payment_cancelled, name='payment_cancelled'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('cart/', views.request_to_paypal, name='request_to_paypal')
]
