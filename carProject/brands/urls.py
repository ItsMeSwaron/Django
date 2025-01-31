from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addBrandsCreateView.as_view(), name='addBrands')
]