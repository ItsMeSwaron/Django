from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.

def addMusician(request):
    if request.method == 'POST':
        musician_Form = forms.musicianForm(request.POST)
        if musician_Form.is_valid():
            musician_Form.save()
            return redirect('addMusician')
    else:
        musician_Form = forms.musicianForm()

    return render(request, 'addMusician.html', {'form':musician_Form})

def editMusician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician_Form = forms.musicianForm(instance=musician)
    if request.method == 'POST':
        musician_Form = forms.musicianForm(request.POST, instance=musician)
        if musician_Form.is_valid():
            musician_Form.save()
            return redirect('homePage')

    return render(request, 'addMusician.html', {'form':musician_Form})