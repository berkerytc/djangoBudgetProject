from unicodedata import category
from django.db import models
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=100,null=True)
    slug = models.SlugField(max_length=100,unique=True,null=True)

    def __str__(self):
        return self.name
    

class Transaction(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=150,null=True)
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(default=now)

