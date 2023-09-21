from django.db import models
from django.utils.text import slugify
from locations.models import Location

placeholder = " "


class Place(models.Model):
    """
    Model for creation of a Place.
    """

    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="places"
    )
    venue_id = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    sub_categories = models.JSONField(null=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    location_string = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    image = models.CharField(max_length=150, default=placeholder)
    ranking_position = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)
    phone = models.CharField(max_length=50, null=True)
    address = models.JSONField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    website = models.CharField(max_length=200, null=True)
    ranking_string = models.CharField(max_length=150, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-ranking_position"]

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
