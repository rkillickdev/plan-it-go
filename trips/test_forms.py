from django.test import TestCase
from .forms import TripForm


class TestTripForm(TestCase):
    """
    Test for trip forms
    """

    def test_trip_form_valid(self):
        """
        Tests if trip form is valid.
        """
        form = TripForm({"title": "Berlin 2023", "slug": "berlin-2023"})
        self.assertTrue(form.is_valid())
