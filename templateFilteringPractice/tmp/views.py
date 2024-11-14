from django.shortcuts import render

# Create your views here.

def home(request):
    d = {'Author' : 'Swaron', 'Age' : 22, 'Arr' : [1439,5,3,2,7], 'List' : 
            [
                {
                    'Name' : 'Fowad', 'Age' : 40, 'CGPA' : 2.90
                },
                {
                    'Name' : 'Amirul', 'Age' : 30, 'CGPA' : 3.98
                },
                {
                    'Name' : 'Dipto', 'Age' : 20, 'CGPA' : 3.50
                }
            ]
        }
    return render(request, 'home.html', context=d)