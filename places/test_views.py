from django.test import TestCase, Client
from django.shortcuts import reverse

from django.contrib.auth.models import User
from profiles.models import Profile
from .models import Place, Review, Image
from locations.models import Location


class TestPlacesViews(TestCase):
    """
    Testing Places Views
    """

    def setUp(self):
        """
        Setup creates user, alt user, profile,
        location, place, review and image.
        """

        self.client = Client()

        self.user = User.objects.create_user(
            username="testuser", email="test@test.com", password="testpassword"
        )
        self.user_alt = User.objects.create_user(
            username="testuseralt",
            email="testalt@test.com",
            password="alttestpassword",
        )
        self.profile = Profile.objects.get(user=self.user)

        self.location = Location.objects.create(
            city="London",
            slug="london",
            summary="The Big Smoke",
            latitude=51.509865,
            longitude=-0.118092,
        )

        self.place = Place.objects.create(
            location=self.location,
            venue_id="1",
            category="restaurant",
            name="London Eye",
            slug="london-eye",
            description="Test Info",
            rating=4.5,
            address="place address",
            latitude=51.503399,
            longitude=-0.119519,
        )

        self.review = Review.objects.create(
            place=self.place, profile=self.profile, body="test review"
        )
        self.image = Image.objects.create(
            profile=self.profile, place=self.place
        )

    def test_list_places(self):
        """
        Tests that place list page renders
        """

        response = self.client.get(
            reverse(
                "place_list",
                kwargs={
                    "location_id": self.location.id,
                    "slug": self.location.slug,
                },
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "places/place_list.html")

    def test_place_browse_detail(self):
        """
        Test that reviews and images are included in the context
        returned by the browse detail view.
        """

        response = self.client.get(
            reverse(
                "place_browse_detail",
                kwargs={
                    "slug": self.place.slug,
                    "pk": self.place.id,
                },
            )
        )
        self.assertIn("reviews", response.context)
        self.assertIn("images", response.context)
