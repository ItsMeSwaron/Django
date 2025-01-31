from django.shortcuts import render, redirect
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from cars.models import Cars
from . import forms
from django.urls import reverse_lazy

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_Form = forms.registrationForm(request.POST)
        if register_Form.is_valid():
            register_Form.save()
            messages.success(request, 'Account created successfully') 
            return redirect('login')
    else:
        register_Form = forms.registrationForm()

    return render(request, 'register.html', {'form':register_Form, 'type':'Register'})

@login_required
def editOwner(request):
    if request.method == 'POST':
        owner_Form = forms.changeUserForm(request.POST, instance=request.user)
        if owner_Form.is_valid():
            owner_Form.save()
            messages.success(request, 'Profile updated successfully') 
            return redirect('profile')
    else:
        owner_Form = forms.changeUserForm(instance=request.user)

    return render(request, 'editOwner.html', {'form':owner_Form})


class userLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully') 
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Information provided is incorrect') 
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'login'
        return context
    
@login_required
def profile(request):
    purchased_cars = request.user.purchased_cars.all() 
    return render(request, 'profile.html', {'cars': purchased_cars})

def passwordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully') 
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'passwordChange.html', {'form':form})    

def userLogout(request):
    logout(request)
    return redirect('login')
