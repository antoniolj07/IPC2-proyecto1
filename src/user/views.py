from django.shortcuts import render
from .models import User

# Create your views here.
def user_detail_view(request, *args, **kwards):
    return render(request, 'user/info.html', {})

def register_view(request, *args, **kwargs):
    return render(request, 'user/register.html', {})

def register_empresa_view(request, *args, **kwargs):
    return render(request, 'user/register-empresa.html', {})

def login_view(request, *args, **kwards):
    return render(request, 'user/login.html', {})