from django.contrib.auth.models import AbstractUser # new
from django.db import models

# Create your models here.

class CustomUser(AbstractUser): # new entire file
    pass

    def __str__(self):
        return 'User: ' + self.email

class UserInfo(CustomUser):
    lname_prefix = models.CharField(max_length = 60, null = True)
    image = models.ImageField(null = True)
    address_street_name = models.CharField(max_length = 60, null = True)
    address_house_nr = models.CharField(max_length = 60, null = True)
    address_house_nr_addition = models.CharField(max_length = 60, null = True)
    address_postcode = models.CharField(max_length = 60, null = True)
    address_city = models.CharField(max_length = 60, null = True)
    address_country = models.CharField(max_length = 60, null = True)
    language = models.CharField(max_length = 60, null = True, default = 'English')