from django.shortcuts import render
from album.models import Album

def homepage(request):
    data = Album.objects.all()
    return render(request, 'homepage.html', {'data':data})