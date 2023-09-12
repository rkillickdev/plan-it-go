from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Model for creation of a Profile
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    screen_name = models.CharField(max_length=15, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    date_of_birth = models.DateField()
    about = models.TextField(blank=True)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        """
        Returns the username as a string representation for each instance
        of the Profile model.
        """
        return str(self.user)
