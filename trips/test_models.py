from django.test import TestCase
from django.contrib.auth.models import User
from .models import Trip, Location, Profile


class TestTripModel(TestCase):
    """
    Tests Trip Model
    """

    def setUp(self):
        """
        Create a user, location, profile and trip.
        """

        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpassword",
        )
        self.location = Location.objects.create(
            city="London",
            slug="london",
            summary="The Big Smoke",
            latitude=51.509865,
            longitude=-0.118092,
        )
        self.profile = Profile.objects.get(user=self.user)
        self.trip = Trip.objects.create(
            profile=self.profile,
            location=self.location,
            title="City Sightseeing",
            slug="city-sightseeing",
        )

        self.expected_str = self.trip.title
        self.number_of_expected_places = self.trip.places.count()

    def test_trip_model(self):
        """
        Tests the attibutes in the Trip model.
        """

        self.assertEqual(self.trip.profile.user.username, "testuser")
        self.assertEqual(self.trip.location.city, "London")
        self.assertEqual(self.trip.title, "City Sightseeing")
        self.assertEqual(self.trip.slug, "city-sightseeing")
        self.assertEqual(str(self.trip), self.expected_str)
        self.assertEqual(
            self.trip.number_of_places(), self.number_of_expected_places
        )
