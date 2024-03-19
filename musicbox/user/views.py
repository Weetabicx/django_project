from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            return redirect('album:search', query)
        else:
            messages.error(request, 'Please enter a search query')
    return render(request, 'user/index.html')


def login(request):
    return render(request, 'user/login.html')


def register(request):
    return render(request, 'user/register.html')