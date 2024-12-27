from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.

# def addAuthor(request):
#     if request.method == 'POST':
#         author_Form = forms.authorForm(request.POST)
#         if author_Form.is_valid():
#             author_Form.save()
#             return redirect('addAuthor')
#     else:
#         author_Form = forms.authorForm()

#     return render(request, 'addAuthor.html', {'form':author_Form})

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

def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            userName = form.cleaned_data.get('username')
            userPass = form.cleaned_data.get('password')
            user = authenticate(username=userName, password=userPass)
            if user is not None:
                messages.success(request, 'Logged in successfully') 
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Invalid username or password')
                return redirect('register')
    else:
        form = AuthenticationForm()

    return render(request, 'register.html', {'form':form, 'type':'Login'})

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data':data})

@login_required
def editProfile(request):
    if request.method == 'POST':
        profile_Form = forms.changeUserForm(request.POST, instance=request.user)
        if profile_Form.is_valid():
            profile_Form.save()
            messages.success(request, 'Profile updated successfully') 
            return redirect('profile')
    else:
        profile_Form = forms.changeUserForm(instance=request.user)

    return render(request, 'updateProfile.html', {'form':profile_Form})

def passChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully') 
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'passChange.html', {'form':form})    

def userLogout(request):
    logout(request)
    return redirect('login')