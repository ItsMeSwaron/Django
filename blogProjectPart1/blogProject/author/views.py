from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def addAuthor(request):
    if request.method == 'POST':
        author_Form = forms.authorForm(request.POST)
        if author_Form.is_valid():
            author_Form.save()
            return redirect('addAuthor')
    else:
        author_Form = forms.authorForm()

    return render(request, 'addAuthor.html', {'form':author_Form})