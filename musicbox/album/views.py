from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumForm, AlbumCommentForm
from django.contrib.auth.decorators import login_required
from .models import Album, Album_Comment
from song.models import Song
from django.urls import reverse
from song.forms import SongForm


# Create your views here.

def albums_list(request):
    albums = Album.objects.all()
    for album in albums:
        album.songs = Song.objects.filter(album=album)
    return render(request, 'album/albums_list.html', {'albums': albums})


# @login_required
def upload_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album:list')
    else:
        form = AlbumForm()
    return render(request, 'album/upload_album.html', {'form': form})


# @login_required
def delete_album(request, album_id):
    if request.method == 'POST':
        album = get_object_or_404(Album, pk=album_id)
        album.delete()
        return redirect(reverse('album:list'))  # Redirect to the album list or wherever you prefer
    else:
        return redirect(reverse('album:details', kwargs={'album_id': album_id}))


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    comments = Album_Comment.objects.filter(album=album)
    song_form = SongForm()
    comment_form = AlbumCommentForm()
    if request.method == "POST":
        form = AlbumCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.album = album
            comment.author = request.user
            comment.save()
            return redirect('album:details', album_id=album.id)
        elif 'song_submit' in request.POST:
            song_form = SongForm(request.POST)
            if song_form.is_valid():
                new_song = song_form.save(commit=False)
                new_song.album = album
                new_song.save()
                return redirect('album:details', album_id=album.id)
    context = {
            'album': album,
            'songs': Song.objects.filter(album=album),
            'comments': comments,
            'comment_form': comment_form,
            'song_form': song_form,
    }
    return render(request, 'album/album_detail.html', context)


# @login_required
def edit_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album:details', album_id=album.id)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album/edit_album.html', {'form': form, 'album': album})



