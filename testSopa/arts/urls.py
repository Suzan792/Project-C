from django.conf.urls import urls
from . import views

urlpatterns = [

    path('home/', views.arts_list),
]
