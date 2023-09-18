from django.db import models
from profiles.models import Profile
from locations.models import Location
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
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    # places = models.ManyToManyField(
    #     Place, related_name="trip_place", blank=True
    # )

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.title

    def number_of_places(self):
        return self.places.count()
