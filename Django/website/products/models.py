from django.db import models
from django.utils import timezone
import users.models as users
import art.models as art
import datetime

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 60)
    stock = models.IntegerField(default=None,blank=True, null=True)
    description = models.CharField(max_length = 600)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_photo = models.ImageField(default='default_product.jpg',upload_to='product_pics')
    upload_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'Product: ' + self.product_name + ' Upload date: ' + str(self.upload_date)

class DesignArtCoordinate(models.Model):
    coordinate_left = models.DecimalField(default=10, max_digits=10, decimal_places=3)
    coordinate_top = models.DecimalField(default=10, max_digits=10, decimal_places=3)
    height = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    width = models.DecimalField(default= 300,max_digits=10, decimal_places=3)

class DesignArtFrameCoordinate(models.Model):
    frame_height = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    frame_width = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    frame_coordinate_left = models.DecimalField(default=10, max_digits=10, decimal_places=3)
    frame_coordinate_top = models.DecimalField(default=10, max_digits=10, decimal_places=3)
    frame_border_radius = models.IntegerField(default= 0)
    rotation = models.CharField(max_length=100,default='matrix(1, 0, 0, 1, 0, 0)')

class DesignTextCoordinate(models.Model):
    coordinate_left = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    coordinate_top = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    font = models.CharField(max_length = 300,default='Roboto')
    font_weight = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    font_style =  models.CharField(max_length = 60,default='normal')
    font_color =  models.CharField(max_length = 60,default='black')
    font_size = models.DecimalField(default= 40,max_digits=10, decimal_places=3)
    text =  models.TextField(default='')

class Design(models.Model):
    product = models.ForeignKey( Product,on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(default=1)
    design_photo = models.ImageField(default='design_pics/defaultDesign.png',upload_to='design_pics',null=True,blank=True)
    art = models.ForeignKey(art.Artwork,on_delete=models.CASCADE)
    user = models.ForeignKey(users.UserProfile,on_delete=models.CASCADE,default=None,blank=True, null=True)
    designArtCoordinate = models.ForeignKey(DesignArtCoordinate,on_delete=models.CASCADE)
    designArtFrameCoordinate = models.ForeignKey(DesignArtFrameCoordinate,on_delete=models.CASCADE)
    designTextCoordinate = models.ForeignKey(DesignTextCoordinate,on_delete=models.CASCADE)

    def __str__(self):
        return self.art.artwork_name + '   |   ' + self.product.product_name + '   |  Customized id: ' + str(self.id)
