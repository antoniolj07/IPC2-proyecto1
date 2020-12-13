from django.shortcuts import render
from .models import User

# Create your views here.
def user_detail_view(request):
    return render(request, 'user/info.html', {})