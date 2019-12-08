from django.contrib.auth.models import User
from django.db import models

from products.models import Design
import datetime

# Create your models here.

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
    ('AR', 'Arrived'),
    ('IM', 'In the making'),
    ('SE', 'Sent'),
    ]

    item = models.OneToManyField(Design, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField(("Date"), default=datetime.date.today)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, default='IM')

    def __str__(self):
        return "Order history id: %s" % self.id
