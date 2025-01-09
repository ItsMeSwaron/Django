from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addAlbumView.as_view(), name='addAlbum'),
    path('edit/<int:id>/', views.editAlbumView.as_view(), name='editAlbum'),
    path('delete/<int:id>/', views.deleteAlbum, name='deleteAlbum'),
]