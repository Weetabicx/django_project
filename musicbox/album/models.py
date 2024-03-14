from datetime import timezone, datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30) #E.g:Album,Single,EP
    slug = models.SlugField(unique=True)
    genre = models.CharField(max_length=30)
    release_date = models.DateField()
    artist = models.CharField(max_length=50)
    # TODO - is Cascade the right choice for on_delete?
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.type + self.name)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def newest_album(self):
        return self.objects.order_by('-release_date')

class Album_Comment(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=300)
    
    def __str__(self):
        return self.comment

    def top_albums(self):
        top_albums = {}
        for album in Album.objects.all()[:10]:
            top_albums[album.id] = (Album_Comment.objects.filter(id=album.id).aggregate(models.Avg('rating')))
        return top_albums