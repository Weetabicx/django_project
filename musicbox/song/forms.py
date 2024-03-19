from django import forms
from .models import Song
from album.models import Album
from django.core.exceptions import ValidationError

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'genre', 'artist', 'album']
        widgets = {
            'album': forms.Select(choices=[(album.id, album.name) for album in Album.objects.all()])
        }
