from django.test import TestCase, Client
from django.shortcuts import reverse

from django.contrib.auth.models import User
from profiles.models import Profile
from .models import Place
from locations.models import Location

class TestPlacesViews(TestCase):
    """
    Testing Places Views
    """

    def setUp(self):
        self.user = User.objects.create_superuser(username="test", password="test", email="test@test.com")
        # self.place = Place.objects.create(
            
        # )
        self.location = Location(
            city="London",
            slug="london",
            summary="The Big Smoke",
            latitude=51.509865,
            longitude=-0.118092,
        )
        self.location.save()

    
    def test_list_places(self):
        """
        Tests that place list page renders
        """
        response = self.client.get(
            reverse('place_list', 
                    kwargs={
                        "location_id": self.location.id, 
                        "slug": self.location.slug
                    }
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'places/place_list.html')
