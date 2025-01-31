from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('brands/<slug:brandSlug>/', views.home, name='brandWiseCars'),
    path('cars/', include('cars.urls')),
    path('brands/', include('brands.urls')),
    path('owner/', include('owner.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
