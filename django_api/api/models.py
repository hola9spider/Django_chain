from django.db import models
from django.contrib.auth.models import User

CATEGORIES_CHOICES = (('CAR','Car'),('BIKE','Bike'),('FURNITURE','Furniture'))
class Snippet(models.Model):
    Name = models.CharField(max_length=25,blank=True, default = '')
    Email_ID = models.CharField(max_length=35)
    Phone_number = models.CharField(max_length=12)
    Subject = models.CharField(max_length=20)
    Categories = models.CharField(User,choices=CATEGORIES_CHOICES,default = 'Car',max_length=10)
    Description = models.CharField(max_length=250)

    class Meta:
        ordering = ['Name']