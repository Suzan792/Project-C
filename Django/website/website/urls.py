"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from art import views as art_views
from website import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from products.views import ProductDetailView, ProductDesignEditView
from .views import ArtListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from users import urls as users_urls
# from carts.views import views as cart_views

urlpatterns = [
    path('',include(users_urls)),
    path('admin/', admin.site.urls),
    path('', ArtListView.as_view(), name='home_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('', include('search.urls')),
    path('', include('users.urls')),
    path('', include('art.urls')),
    path('', include('products.urls')),
    # path('products/(?P<slug>[\w]+)/', cart_views.views.update_cart)
    path('contact', views.contact_page, name='contact_page'),
    path('', include('carts.urls')),
    # path('art/', art_views, name='art'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
