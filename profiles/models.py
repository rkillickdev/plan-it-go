from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    screen_name = models.CharField(max_length=15, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    date_of_birth = models.DateField()
    about = models.TextField()
    profile_image = models.CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user
