from django.db import models

# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.categoryName}'