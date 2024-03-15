from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'type', 'genre', 'release_date', 'artist', 'owner']
