from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('This is home of app_1')

def courses(request):
    return HttpResponse('This is courses of app_1.')

def about(request):
    return HttpResponse('This is about page of app_1.')

