from django.shortcuts import render
from .forms import studentForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = studentForm()

    return render(request, 'home.html', {'form':form})