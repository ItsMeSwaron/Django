from django.shortcuts import render
from task.models import Task

def showTasks(request):
    data = Task.objects.all()
    return render(request, 'showTasks.html', {'data':data})