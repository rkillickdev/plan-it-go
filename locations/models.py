from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Location(models.Model):
    """
    Model for creation of a location.
    """

    city = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)
    summary = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    image = CloudinaryField(
        "image",
        default="placeholder",
        folder="/images/locations",
        format="webp",
    )
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-city"]

    def __str__(self):
        """
        Returns the city field as a string representation
        of the object.
        """
        return self.city

    def save(self, *args, **kwargs):
        """
        Populates the slug field with a slugified version
        of the city field.
        https://stackoverflow.com/questions/141487/is-there-an-easy-way-to-populate-slugfield-from-charfield
        """
        self.slug = slugify(self.city)
        super().save(*args, **kwargs)
