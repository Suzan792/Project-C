from django.db import models
from art.models import Artwork

# Create your models here.
class AdvertisementSlide(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='ads_pics')
    art = models.ForeignKey( Artwork,on_delete=models.CASCADE,default=None)
