from django.shortcuts import render, redirect, get_object_or_404
from .models import Song
from .forms import SongForm
from django.contrib import messages
from album.models import Album
from album.forms import AlbumForm


# Create your views here.
def song_list_view(request):
    songs = Song.objects.all().order_by('-uploaded_at')
    return render(request, 'song/song_list.html', {'songs': songs})


# @login_required
def upload_song(request):
    if request.method == 'POST':
        song_form = SongForm(request.POST, request.FILES)
        if song_form.is_valid():
            # If a new album is not being created, save the song directly
            song_form.save()
            messages.success(request, 'Song uploaded successfully.')
            return redirect('song_list')
    else:
        song_form = SongForm()

    return render(request, 'song/upload_song.html', {'form': song_form})


# @login_required
def delete_song(request, song_id):
    if request.method == 'POST':
        song = get_object_or_404(Song, id=song_id)
        song.delete()
        return redirect('song_list')
