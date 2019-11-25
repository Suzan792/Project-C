from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('payment/', views.PaymentView.payment, name='payment'),
    path('payment-done/', views.PaymentView.payment_done, name='payment_done'),
    path('payment-cancelled/', views.PaymentView.payment_canceled, name='payment_cancelled'),
]