from django.shortcuts import render
from . forms import contactForm, StudentData, passwordValidationProject

def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        return render(request, 'about.html', {'name' : name, 'email' : email})
    else:
        return render(request, 'about.html', {'name' : name, 'email' : email})

def submitForm(request):
    return render(request, 'forms.html')

def djangoForm(request):
    
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./app1/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()

    return render(request,'djangoForms.html',{'form' : form})

def StudentForm(request):
    
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()

    return render(request, 'djangoForms.html', {'form' : form})

def passwordValidation(request):

    if request.method == 'POST':
        form = passwordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordValidationProject()

    return render(request, 'djangoForms.html', {'form':form})