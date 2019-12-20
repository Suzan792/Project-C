from django.contrib.auth.models import User
from django.db import models

from products.models import Design
import datetime

# Create your models here.
class OrderProduct(models.Model):
    product_name = models.CharField(max_length = 60, default='')
    product_photo = models.ImageField(default='default_product.jpg', upload_to='order_product_pics')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=24.99)

    def __str__(self):
        return "%s" % self.product_name

class OrderArtwork(models.Model):
    artwork_name = models.CharField(max_length = 60, default='')
    artwork_photo = models.ImageField(default='default_art.png', upload_to='order_art_pics')
    artwork_price = models.DecimalField(max_digits=1000, decimal_places=2, default=24.99)

    def __str__(self):
        return "%s" % self.artwork_name

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
    text_coordinate_left = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    text_coordinate_top = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    text_font = models.CharField(max_length = 300,default='Roboto')
    text_font_weight = models.DecimalField(default= 300,max_digits=10, decimal_places=3)
    text_font_style =  models.CharField(max_length = 60,default='normal')
    text_font_color =  models.CharField(max_length = 60,default='black')
    text_font_size = models.DecimalField(default= 40,max_digits=10, decimal_places=3)
    text =  models.TextField(default='')

    def __str__(self):
        return self.art.artwork_name + '   |   ' + self.product.product_name

class OrderHistory(models.Model):
    ORDER_STATUS_CHOICES = [
        ('AR', 'Arrived'),
        ('IM', 'In the making'),
        ('SE', 'Sent'),
        ('NP', 'Not paid'),
    ]

    design = models.ForeignKey(OrderDesign, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField(("Date"), default=datetime.date.today)
    order_datetime = models.DateTimeField(("DateTime"), default=datetime.datetime.now)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, default='IM', max_length=2)

    def __str__(self):
        return "Order history id: %s" % self.id
