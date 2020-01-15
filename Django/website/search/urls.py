from django.urls import path
from .views import SearchResultsView

urlpatterns = [
    path('search/<query>', SearchResultsView.as_view(), name='search_results'),
    path('search/<query>/<filter>/<category>', SearchResultsView.as_view(), name='search_filter')
]
