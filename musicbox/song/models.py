from django.db import models
from album.models import Album
from django.template.defaultfilters import slugify
from django.utils import timezone


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)
    release_date = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Song_Comment(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='comments', null=True)
    rating = models.IntegerField()
    comment = models.CharField(max_length=300)


    def __str__(self):
        return f"Comment: {self.comment} - Rating: {self.rating}"    
