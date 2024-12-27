from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('category/<slug:categorySlug>/', views.home, name='categoryWisePost'),
    path('author/', include('author.urls')),
    path('posts/', include('posts.urls')),
    path('category/', include('categories.urls')),
]
