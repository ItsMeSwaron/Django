from django.urls import path
from . import views
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.userLogin, name='login'),
    path('login/', views.userLoginView.as_view(), name='login'),
    path('logout/', views.userLogout, name='logout'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.editProfile, name='editProfile'),
    path('profile/edit/passChange/', views.passChange, name='passChange'),
]
