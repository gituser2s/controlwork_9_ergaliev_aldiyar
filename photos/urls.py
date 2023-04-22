from django.urls import path
from photos.views.base import IndexView
from photos.views.photos import PhotoCreateView, PhotoDetailView, PhotoDeleteView, \
    PhotoUpdateView, FavoriteView, FavoriteDeleteView


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("photo/add", PhotoCreateView.as_view(), name="photo_add"),
    path("photo/<int:pk>", PhotoDetailView.as_view(), name="photo_detail"),
    path("photo/<int:pk>/update", PhotoUpdateView.as_view(), name="photo_update"),
    path('photo/<int:pk>/delete', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/<int:pk>/confirm_delete', PhotoDeleteView.as_view(), name='photo_confirm_delete'),
    path('photo/<int:pk>/to-favorite', FavoriteView.as_view(), name='to_favorite'),
    path('photo/<int:pk>/favorite_delete', FavoriteDeleteView.as_view(), name='favorite_delete'),
]
