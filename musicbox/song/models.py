from django.db import models
from album.models import Album
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='_songs', null=True, blank=True)
    release_date = models.DateTimeField(default=timezone.now)
    uploaded_at = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.title

    def average_rating(self):
        average = self.comments.aggregate(Avg('rating'))['rating__avg']
        return round(average, 1) if average is not None else "No ratings yet"

    def get_absolute_url(self):
        return reverse('song:details', kwargs={'song_id': self.id})


class Song_Comment(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='comments', null=True)
    rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    comment = models.CharField(max_length=300)


    def __str__(self):
        return f"Comment: {self.comment} - Rating: {self.rating}"    
