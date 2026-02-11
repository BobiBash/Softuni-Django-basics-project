from django.core.validators import MinValueValidator
from django.db import models

from Wildlife_Expedition_Tracker.animals.models import Animal
from Wildlife_Expedition_Tracker.expeditions.models import Expedition
from .validators import validate_latitude, validate_longitude


# Create your models here.
class Sighting(models.Model):
    expedition = models.ForeignKey(
        Expedition,
        on_delete=models.CASCADE,
        related_name='sightings'
    )

    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='sightings'
    )

    observed_at = models.DateTimeField()

    count = models.PositiveIntegerField()

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        validators=[validate_latitude]
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        validators=[validate_longitude]
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


