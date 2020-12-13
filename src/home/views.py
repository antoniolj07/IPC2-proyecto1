from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hellow world</h1>')  # string of HTML code
    return render(request, 'home/home.html', {})

def nueva_cuenta_view(request, *args, **kwargs):
    return render(request, 'crear-cuenta.html', {})


def about_view(request, *args, **kwargs):
    # return HttpResponse('<h1>About Page</h1>')
    my_context = {
        'my_text': 'this is about me',
        'number': 123,
        'my_list': ['jorge', 'antoino', 'perez', 'ordo;ez', 'fin'],
        'boolin': True
    }
    return render(request, 'about.html', my_context)