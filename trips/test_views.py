from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, reverse_lazy

from django.contrib.auth.models import User
from .models import Trip, Profile, Place, Location
from places.models import Review, Image
from .views import TripBrowse, TripCreateView, PlaceToggle
from .forms import TripForm


class TestTripsViews(TestCase):
    """
    Testing Trips Views
    """

    def setUp(self):
        """
        Setup creates user, profile, trip, place, review and image.
        Place added to the Trip.
        """
        self.client = Client()
        self.factory = RequestFactory()

        self.user = User.objects.create_user(
            username="testuser", email="test@test.com", password="testpassword"
        )
        self.profile = Profile.objects.get(user=self.user)
        self.location = Location.objects.create(
            city="London",
            slug="london",
            summary="The Big Smoke",
            latitude=51.509865,
            longitude=-0.118092,
        )
        self.trip = Trip.objects.create(
            profile=self.profile,
            location=self.location,
            title="City Sightseeing",
            slug="city-sightseeing",
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
        self.trip.places.add(self.place)

    def test_get_queryset(self):
        url = reverse(
            "trip_browse",
            kwargs={
                "location_id": self.location.id,
                "slug": self.location.slug,
            },
        )
        request = self.factory.get(url)
        view = TripBrowse()
        view.setup(
            request, location_id=self.location.id, slug=self.location.slug
        )

        queryset = view.get_queryset()
        self.assertIn(self.trip, queryset)

    # def test_successful_trip_create_form_valid(self):
    #     form_data = {
    #         # 'profile': self.profile,
    #         'location': self.location,
    #         'title': 'The Bright Lights',
    #         'slug': 'the-bright-lights',
    #         'description': 'about the trip'
    #     }
    #     self.client.login(username="testuser", password="testpassword")
    #     response = self.client.post(reverse("create_trip"))
    #     form = TripForm(form_data)
    #     self.assertTrue(form.instance.profile)
    #     self.assertTrue(form.is_valid())

    def test_review_page_and_create_review(self):
        """
        Test that review_create view renders correct page with existing reviews
        and create review works
        """

        # Test GET method
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(
            reverse(
                "review",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                },
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trips/review.html")

        review_data = {
            "place": self.place,
            "profile": self.profile,
            "body": "test review",
        }

        # Test POST method
        response = self.client.post(
            reverse(
                "review",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                },
            ),
            data=review_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trips/review.html")

        new_review = Review.objects.get(id=2)
        self.assertEqual(new_review.place, self.place)
        self.assertEqual(new_review.profile, self.profile)
        self.assertEqual(new_review.body, "test review")

    def test_invalid_review_submission(self):
        """
        Tests response if the review form submitted is not valid
        """

        self.client.login(username="testuser", password="testpassword")
        review_data = {
            "place": self.place,
            "profile": self.profile,
            "body": "",
        }

        response = self.client.post(
            reverse(
                "review",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                },
            ),
            data=review_data,
        )

        # Referenced the following article for testing messages:
        # https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages

        messages = list(response.context["messages"])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "There was an error!")

    def test_review_edit(self):
        """
        """
        self.client.login(username="testuser", password="testpassword")
        review_data = {
            "place": self.place,
            "profile": self.profile,
            "body": "update test review",
        }
        response = self.client.post(
            reverse(
                "edit_review",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                    "review_id": self.review.id
                },
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            "review",
            kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                }
            )
        )
        updated_review = Review.objects.get(id=self.review.id)
        self.assertEqual(
            updated_review.review, "Cracking movie love this movie"
        )


    def test_successful_trip_delete_redirect(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(
            reverse(
                "delete_trip",
                kwargs={"slug": self.trip.slug, "trip_id": self.trip.id},
            )
        )
        self.assertRedirects(response, reverse("trip_list"))
        # url = reverse('create_trip')
        # request = self.factory.get(url)
        # view = TripCreateView()
        # view.setup(request)
        # request.user = self.user
        # response = TripCreateView.as_view()(request)
        # self.assertEqual(response.status_code, 200)

    def test_toggle_add_place_to_trip(self):
        """
        Clears places for trip and tests adding place to a trip
        """
        self.trip.places.clear()
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(
            reverse(
                "toggle_place",
                kwargs={"trip_id": self.trip.id, "place_id": self.place.id},
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.place in self.trip.places.all())

    def test_toggle_remove_place_from_trip(self):
        """
        Tests removing place from trip
        """
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(
            reverse(
                "toggle_place",
                kwargs={"trip_id": self.trip.id, "place_id": self.place.id},
            )
        )
        self.assertRedirects(
            response,
            reverse(
                "place_detail",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                },
            ),
        )
        self.assertFalse(self.place in self.trip.places.all())

    def test_remove_place_from_itinerary(self):
        """
        Tests removing place from itinerary
        """
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(
            reverse(
                "remove_place",
                kwargs={"trip_id": self.trip.id, "place_id": self.place.id},
            )
        )
        self.assertRedirects(
            response,
            reverse(
                "trip_detail",
                kwargs={"slug": self.trip.slug, "trip_id": self.trip.id},
            ),
        )
        self.assertFalse(self.place in self.trip.places.all())
