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
    owner = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.type + self.name)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Album_Comment(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(300)
    

    def __str__(self):
        return self.title
