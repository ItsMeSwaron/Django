from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    d = {'Author' : 'Swaron', 'Age' : 27, 'Today' : datetime.datetime.now(), 'val' : '', 'lst' : [1,2,3], 'courses' : 
            [
                {
                    'name' : 'amirulz',
                    'cg' : 3.999
                },
                {
                    'name' : 'Ejaz',
                    'cg' : 3.45
                },
                {
                    'name' : 'dipto',
                    'cg' : 3.00
                }
            ]
        }
    
    return render(request, 'home.html', context=d)
