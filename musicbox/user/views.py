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

    carouselAlbums1 = Album.objects.order_by('-release_date')[:3]
    carouselAlbums2 = Album.objects.order_by('-release_date')[3:6]
    carouselAlbums3 = Album.objects.order_by('-release_date')[6:9]
    
    topAlbumsTuples = Album.top_albums()
    topAlbums = []
    for albumTuple in topAlbumsTuples:
        topAlbums.append(albumTuple[0])
        
    topSongsTuples = Song.top_songs()
    topSongs = []
    for songTuple in topSongsTuples:
        topSongs.append(songTuple[0])

    context_dic={}
    context_dic['carousel1'] = carouselAlbums1
    context_dic['carousel2'] = carouselAlbums2
    context_dic['carousel3'] = carouselAlbums3
    context_dic['topAlbums'] = topAlbums
    context_dic['topSongs'] = topSongs

    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            return redirect('album:search', query)
        else:
            messages.error(request, 'Please enter a search query')
            
    return render(request, 'user/index.html', context=context_dic)


def login(request):
    return render(request, 'user/login.html')


def register(request):
    return render(request, 'user/register.html')


def search(request):
    query = request.GET.get('q', '')
    songs = Song.objects.filter(title__icontains=query) | Song.objects.filter(artist__icontains=query)
    albums = Album.objects.filter(name__icontains=query) | Album.objects.filter(artist__icontains=query)

    # 如果你有一个专门的Artist模型
    # artists = Artist.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'songs': songs,
        'albums': albums,
        # 'artists': artists,
    }

    return render(request, 'search_results.html', context)
    
@login_required
def user_profile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    return render(request, 'user_profile.html', {'user_profile': user_profile})