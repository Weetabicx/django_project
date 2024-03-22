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
    if request.user.is_authenticated:
        logged_user=User.objects.get(username=request.user.username)
        user_form=UserForm(request.POST or None, instance=logged_user)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            auth_login(request, logged_user) 
            messages.success(request, ("Profile Updated Successfully"))
            return(redirect('user:index'))
        
        return render(request, 'user/manage_account.html', context = {'user_form': user_form})
    else:
        return HttpResponse("You can only modify profiles which you are logged into.")

    
@login_required
def user_profile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    return render(request, 'user/user_profile.html', {'user_profile': user_profile})

@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse('user:index'))
    
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