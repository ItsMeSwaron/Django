from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showTasks, name='showTasks'),
    path('tasks/', include('task.urls')),
    path('categories/', include('category.urls')),
]
