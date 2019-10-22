from django.db import models

import users, art
import datetime

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 60)
    stock = models.IntegerField()
    description = models.CharField(max_length = 600)
    price = models.IntegerField()
    product_photo = models.ImageField()
    upload_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'Product: ' + self.product_name + ' Upload date: ' + self.upload_date

class Order(models.Model):
    user_id = models.ForeignKey(users.User)
    product_id = models.ForeignKey(Product)
    artwork_id = models.ForeignKey(art.Artwork)
    order_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'Order: ' + self.ID + ' Order date: ' + self.order_date
