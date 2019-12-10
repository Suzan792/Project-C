from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('order/', views.return_orders, name='order_page'),
]
