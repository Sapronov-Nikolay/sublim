from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

class Main(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
         return self.name

    class MPTTMeta:
         order_insertion_by = ['name']

     