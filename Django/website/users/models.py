from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lname_prefix = models.CharField(max_length = 60, null = True, blank = True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_role = models.CharField(max_length = 60, default = 'Customer')
    street_name = models.CharField(max_length = 60, null = True, blank = True)
    house_nr = models.CharField(max_length = 60, null = True, blank = True)
    addition = models.CharField(max_length = 60, null = True, blank = True)
    postcode = models.CharField(max_length = 60, null = True, blank = True)
    city = models.CharField(max_length = 60, null = True, blank = True)
    country = models.CharField(max_length = 60, null = True, blank = True)
    language = models.CharField(max_length = 60, default = 'English')
    sign_up_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return 'User: ' + self.user.username
