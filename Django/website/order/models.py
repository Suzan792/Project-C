from django.contrib.auth.models import User
from django.db import models

import datetime

# Create your models here.
class OrderHistoryItem(models.Model):
    ORDER_STATUS_CHOICES = [
        ('AR', 'Arrived'),
        ('IM', 'In the making'),
        ('SE', 'Sent'),
        ('NP', 'Not paid'),
    ]
    
    name = models.CharField(max_length = 60)
    design_photo = models.ImageField(default='design_pics/defaultDesign.png',upload_to='order_pics')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField(("Date"), default=datetime.date.today)
    order_datetime = models.DateTimeField(("DateTime"), default=datetime.datetime.now)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, default='IM', max_length=2)
    paid_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
