from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.

def addAlbum(request):
    if request.method == 'POST':
        album_Form = forms.albumForm(request.POST)
        if album_Form.is_valid():
            album_Form.save()
            return redirect('homePage')
    else:
        album_Form = forms.albumForm()

    return render(request, 'addAlbums.html', {'form':album_Form})

def editAlbum(request, id):
    album = models.Album.objects.get(pk=id)
    album_Form = forms.albumForm(instance=album)
    if request.method == 'POST':
        album_Form = forms.albumForm(request.POST, instance=album)
        if album_Form.is_valid():
            album_Form.save()
            return redirect('homePage')

    return render(request, 'addAlbums.html', {'form':album_Form})

def deleteAlbum(request, id):
    post = models.Album.objects.get(pk=id)
    post.delete()
    return redirect('homePage')