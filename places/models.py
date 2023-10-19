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
    sub_categories = models.JSONField(null=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    location_string = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    image = models.CharField(max_length=150, default='placeholder')
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
    title = models.CharField(max_length=50, default='Loved It')
    body = models.TextField()
    user_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
        )
    recommended = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review For {self.place.name} by {self.profile.user}"


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
        'image',
        default='placeholder',
        transformation={
            'gravity': "auto",
            'crop': "fill",
            'fetch_format': "auto",
            'dpr': "auto",
            'responsive': True,
            'width': "auto"
        },
        folder="/images/places",
        format="webp"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Image For {self.place.name} by {self.profile.user}"
