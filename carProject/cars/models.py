from django.db import models
from brands.models import Brands
from django.contrib.auth.models import User

# Create your models here.

class Cars(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='cars')
    purchasedBy = models.ManyToManyField(User, related_name='purchased_cars', blank=True)
    image = models.ImageField(upload_to="cars/media/uploads/", blank = True, null = True)

    def __str__(self):
        return f'{self.name}'

class Comment(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    body = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} commented'