from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from album.models import Album
from song.models import Song
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def login(request):
    return render(request, 'user/login.html')


def register(request):
    return render(request, 'user/register.html')

def search_results(request):
    query = request.GET.get('query', '')
    if query:
        songs = Song.objects.filter(Q(title__icontains=query) | Q(artist__icontains=query))
        albums = Album.objects.filter(Q(name__icontains=query) | Q(artist__icontains=query))
        # More query sets can be added for more models like Artist, Genre, etc.
    else:
        songs = Song.objects.all()
        albums = Album.objects.all()
        # More query sets with default listings if needed

    return render(request, 'user/search_results.html', {'songs': songs, 'albums': albums, 'query': query})