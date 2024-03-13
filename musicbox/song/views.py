from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Song
from .forms import SongForm
from django.http import HttpResponseRedirect


# Create your views here.
# views.py
def song_list_view(request):
    songs = Song.objects.all().order_by('-release_date')
    return render(request, 'song/song_list.html', {'songs': songs})


def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            new_song = form.save()
            save_song_info_to_file(new_song)  # Call the function to save song info
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'song/upload_song.html', {'form': form})


def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    song.delete()
    return HttpResponseRedirect(reverse('song_list'))


def save_song_info_to_file(song):
    songs = Song.objects.all()
    with open('song/music_info.txt', 'a') as file:  # Open file in append mode
        for song in songs:
            file.write(f"Name: {song.name}\n")
            file.write(f"Singer: {song.singer}\n")
            file.write(f"Album: {song.album}\n")
            file.write(f"Genre: {song.style}\n")
            file.write(f"Music Link: {song.music_link}\n")
            file.write(f"Average Rating: {song.avgrating}\n")
            file.write(f"Reviews: {song.reviews}\n")
        # Create a string with the song information
        if song.front_cover:
            file.write(f"Cover Image Path: {song.front_cover.url}\n")
        file.write("\n")  # Write the song information to the file
        pass
