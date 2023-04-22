from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import PhotosView, PhotoDetailView, PhotoUpdateView, PhotoDeleteView, PhotoCreateView, FavoriteView


urlpatterns = [
    path("photos/", PhotosView.as_view()),
    path("photos/<int:pk>", PhotoDetailView.as_view()),
    path("photos/create", PhotoCreateView.as_view()),
    path("photos/<int:pk>/update", PhotoUpdateView.as_view()),
    path("photos/<int:pk>/delete", PhotoDeleteView.as_view()),
    path("photos/<int:pk>/delete", PhotoDeleteView.as_view()),
    path("photos/<int:pk>/to-favorite", FavoriteView.as_view()),
    path('login/', obtain_auth_token, name='obtain_auth_token')
]
