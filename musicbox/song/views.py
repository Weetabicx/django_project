from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import SongForm, SongCommentForm
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
            return redirect('song:list')
    else:
        song_form = SongForm()

    return render(request, 'song/upload_song.html', {'form': song_form})


# @login_required
def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    song.delete()
    return redirect('song:list')


def song_detail_view(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    average_rating = song.average_rating()
    print("Average rating is: ", average_rating)
    if request.method == 'POST':
        comment_form = SongCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.song = song
            new_comment.save()
            return redirect('song:detail', song_id=song.id)
    else:
        comment_form = SongCommentForm()
    return render(request, 'song/song_detail.html', {
        'song': song,
        'comment_form': comment_form,
    })


def update_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song:details', song_id=song.id)
    else:
        form = SongForm(instance=song)
    return render(request, 'song/edit_song.html', {'form': form, 'song': song})


def add_comment_to_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if request.method == 'POST':
        form = SongCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.song = song
            comment.save()
            return redirect('song:details', song_id=song.id)
    else:
        form = SongCommentForm()
        return redirect('song:details', song_id=song.id)

def search_song(request):
    query = request.GET.get('q', '')
    if query:
        songs = Song.objects.filter(title__icontains=query)
    else:
        songs = Song.objects.none()
    return render(request, 'song/search_songs.html', {'songs': songs})