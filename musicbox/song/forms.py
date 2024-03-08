from django import forms
from .models import Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['front_cover', 'name', 'singer', 'album', 'style', 'music_link', 'avgrating', 'reviews']
