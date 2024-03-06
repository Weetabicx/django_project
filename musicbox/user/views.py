from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def login(request):
    return render(request, 'user/login.html')


def register(request):
    return render(request, 'user/register.html')