from django.db import models


class Location(models.Model):
    """
    Model for creation of a location.
    """

    city = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    summary = models.TextField()
    latitude = models.DecimalField()
    longtitude = models.DecimalField()
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-city"]

    def __str__(self):
        return self.city
