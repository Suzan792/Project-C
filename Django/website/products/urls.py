from django.urls import path
from .views import ProductDetailView, ProductDesignEditView


urlpatterns = [
path('product/<int:design_pk>/', ProductDetailView.as_view(), name='productDetail_page'),
path('edit/product/<int:art_pk>/', ProductDesignEditView.as_view(), name='editProduct_page'),
]
