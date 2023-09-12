from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save


class Profile(models.Model):
    """
    Model for creation of a Profile
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    screen_name = models.CharField(max_length=15, unique=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        """
        Returns the username as a string representation for each instance
        of the Profile model.
        """
        return self.user.username

# Create a Profile when new user signs up


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)
