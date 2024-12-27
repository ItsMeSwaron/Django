from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.editProfile, name='editProfile'),
    path('profile/edit/passChange/', views.passChange, name='passChange'),
]
