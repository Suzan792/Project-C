from django.contrib.auth.models import User
from django.db import models

from products.models import Design
import datetime

# Create your models here.

class OrderHistory(models.Model):
    ORDER_STATUS_CHOICES = [
        ('AR', 'Arrived'),
        ('IM', 'In the making'),
        ('SE', 'Sent'),
    ]

    item = models.OneToManyField(OrderDesign, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField(("Date"), default=datetime.date.today)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, default='IM')

    def __str__(self):
        return "Order history id: %s" % self.id

class OrderDesign(models.Model):
    # item = models.OneToManyField(Design, null=True, blank=True)
    paid_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=1)

    product = models.ForeignKey(OrderProduct,on_delete=models.CASCADE)
    art = models.ForeignKey(OrderArtwork,on_delete=models.CASCADE)
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
        return "Order history id: %s" % self.id

class OrderProduct(models.Model):
    product_photo = models.ImageField(default='default_product.jpg',upload_to='product_pics')

class OrderArtwork(models.Model):
    artwork_photo = models.ImageField(default='default_art.png',upload_to='art_pics')

