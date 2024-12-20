from django.db import models
from category.models import Category

# Create your models here.

class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    isCompleted = models.BooleanField(default=False) 
    taskAssignDate = models.DateField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.taskTitle}'
