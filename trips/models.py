from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from profiles.models import Profile
from locations.models import Location
from places.models import Place
from cloudinary.models import CloudinaryField


class Trip(models.Model):
    """
    Model for creation of a Trip.
    """

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="trips"
    )
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="trips"
    )
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    trip_image = CloudinaryField('image', default='placeholder')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    places = models.ManyToManyField(
        Place, related_name="trip_place", blank=True
    )

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.title

    def number_of_places(self):
        return self.places.count()

    """
     Populates the slug field with a slugified version
     of the title field.
     https://stackoverflow.com/questions/141487/is-there-an-easy-way-to-populate-slugfield-from-charfield
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
