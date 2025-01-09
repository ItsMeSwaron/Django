from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addMusicianView.as_view(), name='addMusician'),
    path('edit/<int:id>/', views.editMusicianUpdateView.as_view(), name='editMusician'),
    path("register/", views.register, name='register'),
    path('login/', views.userLoginView.as_view(), name='login'),
    path('logout/', views.userLogout, name='logout'),
]