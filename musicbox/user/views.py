from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from forms import UserForm, UserProfileForms

# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def login(request):
    return render(request, 'user/login.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        #NOT a http post, just display the form empty
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'user/register.html',
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})