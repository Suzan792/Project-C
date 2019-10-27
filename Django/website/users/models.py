from django.db import models
from django.contrib.auth.models import User as UserProfile
import datetime

# Create your models here.
class User(models.Model):
    UserProfile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    fname = models.CharField(max_length = 60)
    lname_prefix = models.CharField(max_length = 60, null = True)
    lname = models.CharField(max_length = 60)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    salt = models.IntegerField()
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
        return 'User: ' + self.UserProfile.username
