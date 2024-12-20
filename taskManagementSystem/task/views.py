from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.

def addTask(request):
    if request.method == 'POST':
        task_Form = forms.taskForm(request.POST)

        if task_Form.is_valid():
            task_Form.save()
            return redirect('showTasks')
    else:
        task_Form = forms.taskForm()

    return render(request,'addTask.html',{'form':task_Form})

def editTask(request,id):
    task = models.Task.objects.get(pk=id)
    task_Form = forms.taskForm(instance=task)

    if request.method == 'POST':
        task_Form = forms.taskForm(request.POST, instance=task)

        if task_Form.is_valid():
            task_Form.save()
            return redirect('showTasks')

    return render(request,'addTask.html',{'form':task_Form})

def deleteTask(request, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('showTasks')