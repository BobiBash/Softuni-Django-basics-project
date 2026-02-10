from django.db import models
from django.utils.text import slugify


# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    kingdom = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    food = models.CharField(max_length=100)
    most_distinctive_feature = models.CharField(max_length=150)
    weight = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)
