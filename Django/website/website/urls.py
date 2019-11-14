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
from users import views as user_views
from website import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from .views import ArtListView, ArtDetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register_page'),
    path('profile/', user_views.profile, name='profile_page'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout_page'),
    path('', ArtListView.as_view(), name='home_page'),
    path('art/<int:pk>/', ArtDetailView.as_view(), name='artDetail_page'),
    path('contact', views.contact_page, name='contact_page'),
    re_path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    re_path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('^', include('django.contrib.auth.urls')),
    # path('forgotten_password', user_views.forgotten_password, name='forgotten_password_page'),

    # path('art/', art_views, name='art'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
