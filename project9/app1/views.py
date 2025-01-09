from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.

def home(request):
    response = render(request, 'home.html')
    # response.set_cookie('name', 'Amirul', max_age=5) 
    response.set_cookie('name', 'Amirul', expires=datetime.utcnow()+timedelta(days=7)) 
    return response

def getCookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'getCookie.html', {'name': name})

def deleteCookie(request):
    response = render(request, 'delCookie.html')
    response.delete_cookie('name')
    return response

def setSession(request):
    data = {
        'name' : 'Amirul',
        'age' : 22,
        'language' : 'Bangle'
    }
    print(request.session.get_session_cookie_age())
    request.session.update(data)
    return render(request, 'home.html')

def getSession(request):
    if 'name' in request.session:
        name = request.session.get('name', 'Guest')
        age = request.session.get('age')
        request.session.modified = True
        return render(request, 'getSession.html', {'name':name, 'age':age})
    else:
        return HttpResponse('Session has expired. Please login again')

def deleteSession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delCookie.html')