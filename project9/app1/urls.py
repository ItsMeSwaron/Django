from django.urls import path
from . import views

urlpatterns = [
    path('', views.setSession),
    path('get/', views.getSession),
    path('del/', views.deleteSession),
]
