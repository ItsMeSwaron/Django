from django.shortcuts import render, redirect
from . import forms 

# Create your views here.

def addCategory(request):
    if request.method == 'POST':
        category_Form = forms.categoryForm(request.POST)
        if category_Form.is_valid():
            category_Form.save()
            return redirect('addCategory')
    else:
        category_Form = forms.categoryForm()

    return render(request,'addCategory.html',{'form':category_Form})