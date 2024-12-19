from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addAlbum, name='addAlbum'),
    path('edit/<int:id>', views.editAlbum, name='editAlbum'),
    path('delete/<int:id>', views.deleteAlbum, name='deleteAlbum')
]
