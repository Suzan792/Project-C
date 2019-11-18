from django.db import models

import users.models as users
import datetime

# Create your models here.
class Artwork(models.Model):
    artwork_name = models.CharField(max_length = 60)
    artist = models.ForeignKey(users.UserProfile, on_delete = models.SET('unknown'))
    artwork_description = models.CharField(max_length = 600)
    artwork_likes = models.ManyToManyField(users.UserProfile,related_name="likes",blank=True)
    artwork_photo = models.ImageField(default='default_art.png',upload_to='art_pics')
    upload_date_time = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'Artwork: ' + self.artwork_name

class Comment(models.Model):
    commenter = models.ForeignKey(users.UserProfile, on_delete = models.SET('unknown'))
    artwork = models.ForeignKey(Artwork, on_delete = models.SET('deleted'))
    comment = models.CharField(max_length = 600)
    upload_date_time = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'Comment for artwork: ' + self.artwork_id + ', ' + self.comment_date + ' ' + self.ID
