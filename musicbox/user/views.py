from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserEditForm


def index(request):
    return render(request, 'user/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(1209600)
            return redirect(f'/{user.username}/user/')
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username or password'})
    return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'user/register.html', {'error': 'Username already exists'})
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect(f'/{user.username}/user/')
    return render(request, 'user/register.html')


@login_required
def manage_account(request, username):
    if request.user.username != username:
        return redirect('some_error_page')

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(f'/{request.user.username}/myaccount/')
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'user/manage_account.html', {'form': form})



