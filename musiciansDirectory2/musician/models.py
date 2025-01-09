from django.db import models

# Create your models here.

class Musician(models.Model):

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=12)
    instrumentType = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'