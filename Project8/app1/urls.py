from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('passChange/', views.passChange, name='passChange'),
    path('passChange2/', views.passChange2, name='passChange2'),
    path('profile/', views.profile, name='profile'),
]
