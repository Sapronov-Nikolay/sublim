from django.db import models
from datetime import datetime

class Good(models.Model):
    picture = models.ImageField()
    namegood = models.CharField(max_length=30)
    specification = models.CharField(max_length=300)
    price = models.FloatField()

def __str__(self):
    return str(self.namegood)