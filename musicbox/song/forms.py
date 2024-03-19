from django import forms
from .models import Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['album', 'title', 'genre', 'release_date', 'artist']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }