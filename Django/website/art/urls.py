from django.urls import path
from .views import upload_art , artistworkListView, ArtDetailView , deleteArtView , ArtworkUpdateView, ArtworkLikeListView

urlpatterns = [
path('art/<int:pk>/', ArtDetailView.as_view(), name='artDetail_page'),
path('art/<int:pk>/update/', ArtworkUpdateView.as_view(), name='artUpdate_view'),
path('art/<int:pk>/delete', deleteArtView.as_view(), name='artDelete_view'),
path('artistwork/',artistworkListView.as_view(),name = 'artistwork'),
path('artistwork/likes/<int:pk>',ArtworkLikeListView.as_view(),name = 'artworkLikeList_page'),
path('upload', upload_art, name='upload_art'),
]
