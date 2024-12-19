from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addMusician, name='addMusician'),
    path('edit/<int:id>', views.editMusician, name='editMusician')
]
