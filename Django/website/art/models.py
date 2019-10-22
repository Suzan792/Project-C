from django.db import models
import users
import datetime

# Create your models here.
class Artwork(models.Model):
    artwork_name = models.CharField(max_length = 60)
    artist_id = models.ForeignKey(users.User)
    artwork_description = models.CharField(max_length = 600)
    artwork_likes = models.IntegerField()
    artwork_photo = models.ImageField()
    upload_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'Artwork: ' + self.artwork_name + ' Upload date: ' + self.upload_date

class Comment(models.Model):
    artist_id = models.ForeignKey(users.User)
    artwork_id = models.ForeignKey(Artwork)
    comment = models.CharField(max_length = 600)
    comment_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'Comment for artwork: ' + self.artwork_id + ', ' + self.comment_date + ' ' + self.ID
