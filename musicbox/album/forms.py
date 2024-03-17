from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['cover','name', 'type', 'genre', 'release_date', 'artist']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
