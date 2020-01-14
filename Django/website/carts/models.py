from django.db import models
from products.models import Design
from users.models import User


class Cart(models.Model):
    item = models.ManyToManyField(Design, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Cart id: %s" % self.id

class Wish(models.Model):
    item = models.ManyToManyField(Design, null=True, blank=True)
    user =  models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return "Wish list id: %s" % self.id
