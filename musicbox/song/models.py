from django.db import models
from musicbox.album.models import Album

# Create your models here.
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    release_date=models.DateField() #date/artist are automatically set ot the album's date/artist
    artist = models.CharField(max_length=50)
    

    def __str__(self):
        return self.title

class Song_Comment(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Song, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(300)
    
    def __str__(self):
        return self.title    
