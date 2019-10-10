from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length = 60)
    lname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 60)
    email = models.CharField(max_length = 60)
    password = models.CharField(max_length = 60)
    salt = models.IntegerField()
    user_role = models.CharField(max_length = 60)
    address = models.CharField(max_length = 60)
    country = models.CharField(max_length = 60)
    language = models.CharField(max_length = 60)
    sign_up_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'User: ' + self.username
