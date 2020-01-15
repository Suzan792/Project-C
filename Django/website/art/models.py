from django.db import models
from django.urls import reverse
from django.utils import timezone
import users.models as users
import datetime
import os
from website import settings
# Create your models here.


class Artwork(models.Model):
    artwork_name = models.CharField(max_length = 60)
    artist = models.ForeignKey(users.UserProfile, on_delete = models.CASCADE)
    artwork_description = models.TextField(max_length = 600)
    artwork_likes = models.ManyToManyField(users.UserProfile,related_name="likes",blank=True)
    artwork_price = models.DecimalField(max_digits=1000, decimal_places=2,default=24.99)
    artwork_photo = models.ImageField(default='default_art.png',upload_to='art_pics')
    upload_date_time = models.DateTimeField(default=timezone.now)

    # delete the image from the DB if object is deleted
    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.artwork_photo.storage, self.artwork_photo.path
        # Delete the model before the file
        super(Artwork, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

    def __str__(self):
        return 'Artwork: ' + self.artwork_name


class Comment(models.Model):
    commenter = models.ForeignKey(users.UserProfile, on_delete = models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete = models.CASCADE)
    comment = models.TextField(max_length = 500)
    upload_date_time = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'Comment for artwork: ' + self.comment
