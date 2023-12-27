from django.db import models
from datetime import datetime

class Good(models.Model):
    picture = models.ImageField(default='/static/img/svekla-ee09.jpg')
    namegood = models.CharField(max_length=30)
    specification = models.CharField(max_length=300)
    price = models.FloatField()

def __str__(self):
    return str(self.namegood)