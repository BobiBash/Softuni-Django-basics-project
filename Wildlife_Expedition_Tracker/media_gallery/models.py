from django.db import models



# Create your models here.
class MediaGallery(models.Model):
    expedition = models.ForeignKey("expeditions.Expedition", on_delete=models.CASCADE, related_name="media""")
    image = models.ImageField(upload_to="media_gallery/")
    uploaded_at = models.DateTimeField(auto_now_add=True)