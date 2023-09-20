from django.db import models
from django.utils.text import slugify
from locations.models import Location


class Place(models.Model):
    """
    Model for creation of a Place.
    """

    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="places"
    )
    venue_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    category = models.CharField(max_length=50)
    rank = models.IntegerField()
    tags = models.JSONField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-rank"]

    def __str__(self):
        return self.name

    """
     Populates the slug field with a slugified version
     of the title field.
     https://stackoverflow.com/questions/141487/is-there-an-easy-way-to-populate-slugfield-from-charfield
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
