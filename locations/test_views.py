from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Location


class TestLocationsViews(TestCase):
    """
    Testing Trips Views
    """

    def setUp(self):
        """
        Setup creates user and location.
        """
        self.client = Client()

        self.user = User.objects.create_superuser(
            username="superuser",
            password="supertest",
            email="supertest@test.com",
        )

        self.location = Location.objects.create(
            city="London",
            slug="london",
            summary="The Big Smoke",
            latitude=51.509865,
            longitude=-0.118092,
        )

    def test_create_destination_context_data(self):
        """
        Tests the get_context_data method of CreateDestination View.
        """
        self.client.login(username="superuser", password="supertest")
        response = self.client.get(reverse("locations"))

        self.expected_context = Location.objects.all().order_by("city")
        self.assertQuerysetEqual(
            response.context["destinations"], self.expected_context
        )

    def test_update_destination_context_data(self):
        """
        Tests the get_context_data method of the UpdateDestination View.
        """
        self.client.login(username="superuser", password="supertest")
        response = self.client.get(
            reverse(
                "update_destination",
                kwargs={
                    "location_id": self.location.id,
                    "slug": self.location.slug,
                },
            )
        )

        self.expected_context = Location.objects.all().order_by("city")
        self.assertQuerysetEqual(
            response.context["destinations"], self.expected_context
        )
