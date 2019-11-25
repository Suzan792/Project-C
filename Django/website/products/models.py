from django.db import models

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
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    art = models.ForeignKey(art.Artwork,on_delete=models.CASCADE)
    coordinate_left = models.CharField(max_length=30)
    coordinate_top = models.CharField(max_length=30)
    height = models.IntegerField()
