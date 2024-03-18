from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from PIL import Image
import io
from django.core.files.base import ContentFile


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)  # E.g:Album,Single,EP
    slug = models.SlugField(unique=True)
    genre = models.CharField(max_length=30)
    release_date = models.DateField()
    artist = models.CharField(max_length=50)
    # TODO - is Cascade the right choice for on_delete?
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(
        upload_to='album_covers/',
        validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg', 'png'])], )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.type + '-' + self.name)  # Added a dash for readability
        super(Album, self).save(*args, **kwargs)
        if self.cover:
            img = Image.open(self.cover.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.cover.path)

    def __str__(self):
        return self.name

    def latest_albums() -> models.QuerySet:
        """
        returns the latest five albums
        """
        return Album.objects.order_by('-release_date')[:5]

    def top_albums() -> list[tuple[int, float]]:
        """
        returns the top five albums in the form (album_id, average_rating)
        """
        top_albums = {}
        for album in Album.objects.all():
            top_albums[album] = (Album_Comment.objects.filter(album=album.id).aggregate(models.Avg('rating')))["rating__avg"]
        result = {k: v for k, v in sorted(top_albums.items(), key=lambda item: item[1], reverse=True)}
        return [(k,v) for k,v in result.items()][:5]

class Album_Comment(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=300)
    
    def __str__(self):
        return self.comment