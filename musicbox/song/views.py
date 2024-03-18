from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Song
from django.http import HttpResponseRedirect



# Create your views here.
def song_list_view(request):
    songs = Song.objects.all().order_by('-uploaded_at')
    return render(request, 'song/song_list.html', {'songs': songs})



def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    song.delete()
    return HttpResponseRedirect(reverse('song_list'))

