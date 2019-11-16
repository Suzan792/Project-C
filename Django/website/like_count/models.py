from django.db import models
import users.models as users
import art.models as arts
# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(users.UserProfile, on_delete = models.SET('unknown'))
    art = models.ForeignKey(arts.Artwork, on_delete = models.CASCADE)

    def __str__(self):
        return  self.user.user.username + ' <3 '+ self.art.artwork_name
