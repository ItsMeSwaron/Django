from django.urls import path
from . import views

urlpatterns = [
    # path('add/', views.addPost, name='addPost'),
    path('add/', views.addPostCreateView.as_view(), name='addPost'),
    # path('edit/<int:id>/', views.editPost, name='editPost'),
    path('edit/<int:id>/', views.editPostUpdateView.as_view(), name='editPost'),
    # path('delete/<int:id>/', views.deletePost, name='deletePost'),
    path('delete/<int:id>/', views.deletePostView.as_view(), name='deletePost'),
    path('detail/<int:id>/', views.detailPostView.as_view(), name='detailPost'),
]
