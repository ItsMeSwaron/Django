from django.urls import path
from . import views

urlpatterns = [
    # path('edit/<int:id>/', views.editCarsUpdateView.as_view(), name='editCars'),
    # path('delete/<int:id>/', views.deleteCarsView.as_view(), name='deleteCars'),
    path('detail/<int:id>/', views.detailCarsView.as_view(), name='detailCars'),
    path('buy/<int:car_id>/', views.buyNow, name='buyNow'),
]