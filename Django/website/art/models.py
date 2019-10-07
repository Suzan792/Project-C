from django.db import models

# Create your models here.
class Painting(models.Model):
    painting_name = models.CharField(max_length = 60)
    painter_name = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to='img')
    def __str__(self):
        return 'Painting: ' + self.painting_name

class Testmodel(models.Model):
    test = models.CharField(max_length = 60)
    def __str__(self):
        return 'test: ' + self.test