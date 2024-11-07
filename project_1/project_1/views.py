from django.http import HttpResponse

def home(request):
    return HttpResponse("This is home")

def contact(request):
    return HttpResponse("This is............")