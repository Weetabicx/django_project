from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import UserProfile
from django.shortcuts import render, redirect
from user.forms import UserForm, UserProfileForm
from django.urls import reverse
from django.http import HttpResponse

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect(reverse('user:index'))
            else:
                return HttpResponse("Your MusicBox account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Incorrect username or password. If you don't have an account you can register to create one.")
    else:
        return render(request, 'user/login.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                
            registered=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    
    return render(request, 'user/register.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

@login_required
def manage_account(request):

    if request.method == 'POST':
        current_password = request.post.get('current_password')
        new_password = request.post.get('new_password')

        if(request.user.password==current_password):
           request.user.password=new_password
           return redirect(reverse('user:index'))
        else:
            return HttpResponse("Incorrect password.")
    else:
        return render(request, 'user/manage_account.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse('user:login'))