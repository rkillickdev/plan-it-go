from django.db import models
from .models import Profile
from . models import Location


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
    places = models.ManyToManyField(
        Place, related_name="trip_place", blank=True
    )
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.title

    def number_of_places(self):
        return self.places.count()
