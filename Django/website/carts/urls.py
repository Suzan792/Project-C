from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.view, name='cart'),
    path('payment/<int:product_pk>/<int:art_pk>/', views.payment, name='payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
]
