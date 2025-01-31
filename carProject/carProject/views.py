from django.shortcuts import render
from cars.models import Cars
from brands.models import Brands

def home(request, brandSlug = None):
    cars = Cars.objects.all()

    if brandSlug is not None:
        brand = Brands.objects.get(slug=brandSlug)
        cars = Cars.objects.filter(brand=brand)
    
    brands = Brands.objects.all()
    return render(request, 'home.html', {'car':cars, 'brand':brands})