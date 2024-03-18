from django import forms
from .models import Song
from album.models import Album


class SongForm(forms.ModelForm):
    new_album_name = forms.CharField(max_length=100, required=False, help_text="Or create a new album")

    class Meta:
        model = Song
        fields = ['title', 'genre',  'artist', 'album', 'new_album_name']
        widgets = {
            'album': forms.Select(choices=[(album.id, album.name) for album in Album.objects.all()] + [('new', 'Create New Album')]),
        }