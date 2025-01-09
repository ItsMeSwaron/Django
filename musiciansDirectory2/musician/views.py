from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.contrib import messages
from . import models
from . import forms
from django.urls import reverse_lazy

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_Form = forms.registrationForm(request.POST)
        if register_Form.is_valid():
            register_Form.save()
            messages.success(request, 'Account created successfully') 
            return redirect('register')
    else:
        register_Form = forms.registrationForm()

    return render(request, 'register.html', {'form':register_Form, 'type':'Register'})

class addMusicianView(CreateView):
    model = models.Musician
    form_class = forms.musicianForm
    template_name = 'addMusician.html'
    success_url = reverse_lazy('homepage')

@method_decorator(login_required, name='dispatch')
class editMusicianUpdateView(UpdateView):
    model = models.Musician
    form_class = forms.changeUserForm
    template_name = 'editMusician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

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


def userLogout(request):
    logout(request)
    return redirect('login')