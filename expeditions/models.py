from django.db import models
from django.utils.text import slugify

from common.mixins import SlugMixin
from .validators import validate_text


# Create your models here.
class Expedition(SlugMixin, models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(
        unique=True,
        blank=True,
    )
    target_species = models.ForeignKey(
        "animals.Animal", on_delete=models.CASCADE, related_name="target_expeditions"
    )
    expected_species = models.ManyToManyField(
        "animals.Animal", related_name="expected_expeditions", blank=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=150, validators=[validate_text])
    start_date = models.DateField()
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = self._generate_unique_slug(base_slug)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("expedition_detail", kwargs={"slug": self.slug})

    def is_active(self):
        from django.utils import timezone

        today = timezone.now().date()
        return self.start_date <= today <= self.end_date
