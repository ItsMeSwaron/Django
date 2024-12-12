from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def addProfile(request):
    if request.method == 'POST':
        profile_Form = forms.profileForm(request.POST)
        if profile_Form.is_valid():
            profile_Form.save()
            return redirect('addProfile')
    else:
        profile_Form = forms.profileForm()

    return render(request, 'addProfiles.html', {'form':profile_Form})