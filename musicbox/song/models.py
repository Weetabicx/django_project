from django.db import models
from album.models import Album
from django.template.defaultfilters import slugify


# Create your models here.
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    # TODO - Do both Album and Song need a genre?
    genre = models.CharField(max_length=30)
    release_date = models.DateField()  # date/artist are automatically set ot the album's date/artist
    artist = models.CharField(max_length=50)
    slug = models.SlugField(default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.album}-{self.title}")
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Song_Comment(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title    
