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
from django.urls import path, include
from art import views as art_views
from users import views as user_views
from website import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from art.views import  ArtDetailView
from products.views import ProductDetailView
from .views import ArtListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from art.views import upload_art , artistworkListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register_page'),
    path('profile/', user_views.profile, name='profile_page'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout_page'),
    path('', ArtListView.as_view(), name='home_page'),
    path('art/<int:pk>/', ArtDetailView.as_view(), name='artDetail_page'),
    path('product/<int:product_pk>/<int:art_pk>/', ProductDetailView.as_view(), name='productDetail_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('upload', upload_art, name='upload_art'),
    path('artistwork/',artistworkListView.as_view(),name = 'artistwork')

    # path('art/', art_views, name='art'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
