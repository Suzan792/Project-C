from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('product/<int:design_pk>/', views.ProductDetailView.as_view(), name='productDetail_page'),
    path('edit/product/<int:art_pk>/', views.ProductDesignEditView.as_view(), name='editProduct_page'),
]
