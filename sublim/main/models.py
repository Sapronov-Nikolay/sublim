from django.db import models
from datetime import datetime


class Good(models.Model):
    picture = models.ImageField(upload_to="images/%y/%m/%d/")
    namegood = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    specification = models.CharField(max_length=300)
    price = models.FloatField()


def __str__(self):
    return str(self.namegood)


class Kategory(models.Model):
    kategoriya = models.CharField(max_length=20, unique=True)


def __str__(self):
    return str(self.kategoriya)

class Cart(models.Model):
    picture = models.ImageField(upload_to="images/%y/%m/%d/")
    namegood = models.CharField(max_length=30)
    price = models.FloatField()

def __str__(self):
    return str(self.namegood)