from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField
from locations.models import Location
from profiles.models import Profile


class Place(models.Model):
    """
    Model for creation of a Place.
    """

    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="places"
    )
    venue_id = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=150, null=True)
    category = models.CharField(max_length=150)
    sub_categories = models.JSONField(null=True, blank=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    location_string = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    image = models.CharField(max_length=150, default="placeholder")
    ranking_position = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
    phone = models.CharField(max_length=50, null=True)
    address = models.JSONField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    website = models.CharField(max_length=200, null=True)
    ranking_string = models.CharField(max_length=150, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["-ranking_position"]

    def __str__(self):
        """
        Returns the name as a string representation
        of the object.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Populates the slug field with a slugified version
        of the title field. Referenced this article:
        https://stackoverflow.com/questions/141487/is-there-an-easy-way-to-populate-slugfield-from-charfield
        """
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Review(models.Model):
    """
    Model for creation of a Review.
    """

    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="reviews"
    )
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="reviews"
    )
    body = models.TextField()
    user_rating = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    recommended = models.BooleanField(default=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns the place name and city as a string representation
        of the object.
        """
        return f"Review For {self.place.name}, {self.place.location.city}"


class Image(models.Model):
    """
    Model for storage of user uploaded images.
    Referenced the following article for CloudinaryField transformations:
    https://cloudinary.com/documentation/django_image_manipulation#apply_common_image_transformations
    """

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="images"
    )
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="images"
    )
    path = CloudinaryField(
        "image",
        transformation={
            "fetch_format": "auto",
            "quality": "auto",
            "dpr": "auto",
            "responsive": True,
        },
        folder="/images/places",
        format="webp",
    )
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns the place name as a string representation
        of the object.
        """
        return f"Image For {self.place.name}"
