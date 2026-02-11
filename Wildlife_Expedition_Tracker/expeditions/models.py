from django.db import models
from django.utils.text import slugify


# Create your models here.
class Expedition(models.Model):
    title = models.CharField(
        max_length=150
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
    )
    target_species = models.ForeignKey(
        "animals.Animal",
        on_delete=models.CASCADE,
       related_name="primary_expeditions"
    )
    expected_species = models.ManyToManyField(
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

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = self._generate_unique_slug(base_slug)

        super().save(*args, **kwargs)


    def _generate_unique_slug(self, base_slug):
        slug = base_slug
        counter = 1

        while Expedition.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        return slug