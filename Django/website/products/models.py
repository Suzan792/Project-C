from django.db import models
from django.utils import timezone
import users.models as users
import art.models as art
import datetime

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 60)
    stock = models.IntegerField()
    description = models.CharField(max_length = 600)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_photo = models.ImageField(default='default_product.jpg',upload_to='product_pics')
    upload_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'Product: ' + self.product_name + ' Upload date: ' + str(self.upload_date)

class Order(models.Model):
    user = models.ForeignKey(users.UserProfile, on_delete = models.SET('unknown'))
    product = models.ForeignKey(Product, on_delete = models.SET('deleted'))
    artwork = models.ForeignKey(art.Artwork, on_delete = models.SET('deleted'))
    order_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'Order: ' + self.ID + ' Order date: ' + self.order_date

class Wish(models.Model):
    user = models.ForeignKey(users.UserProfile, on_delete = models.SET('unknown'))
    product = models.ForeignKey(Product, on_delete = models.SET('deleted'))
    artwork = models.ForeignKey(art.Artwork, on_delete = models.SET('deleted'))
    wish_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'Wish: ' + self.ID + ' Wish date: ' + self.wish_date

class Design(models.Model):
    product = models.ForeignKey( Product,on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    art = models.ForeignKey(art.Artwork,on_delete=models.CASCADE)
    user = models.ForeignKey(users.UserProfile,on_delete=models.CASCADE,default=None,blank=True, null=True)
    coordinate_left = models.DecimalField(default=10, max_digits=10, decimal_places=3)
    coordinate_top = models.DecimalField(default=10, max_digits=10, decimal_places=3)
    height = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    width = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    frame_height = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    frame_width = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    frame_coordinate_left = models.DecimalField(default=10, max_digits=10, decimal_places=3)
    frame_coordinate_top = models.DecimalField(default=10, max_digits=10, decimal_places=3)
    frame_border_radius = models.IntegerField(default= 0)
    rotation = models.CharField(max_length=100,default='matrix(1, 0, 0, 1, 0, 0)')
    def __str__(self):
        return self.art.artwork_name + '   |   ' + self.product.product_name + '   |  Customized id: ' + str(self.id)
