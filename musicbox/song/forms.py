from django import forms
from .models import Song, Song_Comment
from album.models import Album
from django.core.exceptions import ValidationError

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'genre', 'artist', 'album']
        widgets = {
         }

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['album'].widget = forms.Select(choices=[(album.id, album.name) for album in Album.objects.all()])

class SongCommentForm(forms.ModelForm):
    class Meta:
        model = Song_Comment
        fields = ['rating', 'comment']