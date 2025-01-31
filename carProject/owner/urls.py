from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.editOwner, name='editOwner'),
    path("register/", views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.userLoginView.as_view(), name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('profile/edit/passwordChange/', views.passwordChange, name='passwordChange'),

]
