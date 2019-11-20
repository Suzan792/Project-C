from django.db import models
from art.model import Artwork
from product.model import Product

# Create your models here.
class Design(models.Model):
    art = models.ForeignKey(Artwork,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
