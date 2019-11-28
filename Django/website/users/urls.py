from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    re_path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    re_path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name="registration\change_password.html"), name='change_password'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name="registration\password_change_done.html"), name='password_change_done'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),        
]