from django.db import models



# Create your models here.
class Expedition(models.Model):
    title = models.CharField(max_length=150)
    animal = models.ForeignKey("animals.Animal", on_delete=models.CASCADE, related_name="expeditions")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.ManyToManyField("locations.Location", blank=True, related_name="expeditions")
    animal_image = models.ImageField(upload_to="expeditions/", blank=True, null=True)