from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=150)
    continent = models.CharField(max_length=50, blank=True)