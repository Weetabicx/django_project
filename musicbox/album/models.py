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
    cover = models.ImageField(
        upload_to='album_covers/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])], )

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

class Album_Comment(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='comments')
    rating = models.IntegerField()
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.comment[:20]