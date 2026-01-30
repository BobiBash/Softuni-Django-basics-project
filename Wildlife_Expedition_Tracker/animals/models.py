from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    kingdom = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    food = models.CharField(max_length=100)
    most_distinctive_feature = models.CharField(max_length=150)
    weight = models.CharField(max_length=50)
