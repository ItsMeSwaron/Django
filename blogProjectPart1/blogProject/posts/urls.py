from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addPost, name='addPost'),
    path('edit/<int:id>', views.editPost, name='editPost'),
    path('delete/<int:id>', views.deletePost, name='deletePost')
]
