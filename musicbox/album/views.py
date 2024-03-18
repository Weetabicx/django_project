from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumForm
from django.contrib.auth.decorators import login_required
from .models import Album
from song.models import Song


# Create your views here.

def albums_list(request):
    albums = Album.objects.all()
    return render(request, 'album/albums_list.html', {'albums': albums})

@login_required
def upload_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('albums_list')
    else:
        form = AlbumForm()
    return render(request, 'album/upload_album.html', {'form': form})

@login_required
def album_update(request, id):
    album = get_object_or_404(Album, id=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('albums_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album/album_form.html', {'form': form})

@login_required
def album_delete(request, id):
    album = get_object_or_404(Album, id=id)
    album.delete()
    return redirect('albums_list')


def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    songs = Song.objects.filter(album=album)
    return render(request, 'album/album_detail.html', {'album': album, 'songs': songs})