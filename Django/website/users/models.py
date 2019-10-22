from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length = 60)
    lname_prefix = models.CharField(max_length = 60, null = True)
    lname = models.CharField(max_length = 60)
    username = models.CharField(max_length = 60)
    email = models.CharField(max_length = 60)
    password = models.CharField(max_length = 60)
    salt = models.IntegerField()
    image = models.ImageField(null = True)
    user_role = models.CharField(max_length = 60)
    street_name = models.CharField(max_length = 60, null = True)
    house_nr = models.CharField(max_length = 60, null = True)
    addition = models.CharField(max_length = 60, null = True)
    postcode = models.CharField(max_length = 60, null = True)
    city = models.CharField(max_length = 60, null = True)
    country = models.CharField(max_length = 60)
    language = models.CharField(max_length = 60, default = 'English')
    sign_up_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'User: ' + self.username
