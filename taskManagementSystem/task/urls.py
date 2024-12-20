from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addTask, name='addTask'),
    path('edit/<int:id>', views.editTask, name='editTask'),
    path('delete/<int:id>', views.deleteTask, name='deleteTask')
]