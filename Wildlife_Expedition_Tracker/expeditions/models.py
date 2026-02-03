from django.db import models



# Create your models here.
class Expedition(models.Model):
    title = models.CharField(
        max_length=150
    )
    primary_animal = models.ForeignKey(
        "animals.Animal",
        on_delete=models.CASCADE,
       related_name="primary_expeditions"
    )
    additional_animals = models.ManyToManyField(
        "animals.Animal",
            related_name="additional_expeditions",
            blank=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    location = models.CharField(
        max_length=150,
    )
    animal_image = models.ImageField(
        upload_to="expeditions/",
        blank=True,
        null=True
    )