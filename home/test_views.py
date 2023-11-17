from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User
from locations.models import Location


class TestHomeViews(TestCase):
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

    def test_home_view(self):
        """
        Tests to see that index.html is returned
        as home page.
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

        self.expected_context = Location.objects.all().order_by("city")
        self.assertQuerysetEqual(
            response.context["destinations"], self.expected_context
        )
