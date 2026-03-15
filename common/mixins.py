from django.db import models



class SlugMixin(models.Model):
    def _generate_unique_slug(self, base_slug):
        slug = base_slug
        counter = 1

        while self.__class__.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        return slug

    class Meta:
        abstract = True