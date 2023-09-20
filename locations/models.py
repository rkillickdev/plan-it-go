from django.db import models
from cloudinary.models import CloudinaryField


class Location(models.Model):
    """
    Model for creation of a location.
    """

    city = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    summary = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    image = CloudinaryField('image', default='placeholder',
                            folder="/images/locations",
                            format="webp"
                            )

    class Meta:
        ordering = ["-city"]

    def __str__(self):
        return self.city
