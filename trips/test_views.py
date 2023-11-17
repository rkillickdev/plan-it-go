from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, reverse_lazy
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from .models import Trip, Profile, Place, Location
from places.models import Review, Image
from .views import TripCreateView, PlaceToggle
from .forms import TripForm


class TestTripsViews(TestCase):
    """
    Testing for Trips Views.
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

    # def test_get_success_url_redirect(self):
    #     """
    #     """
    #     trip_data = {
    #         "profile": self.profile,
    #         "location": self.location,
    #         "title": "West End Shows",
    #         "slug": "west-end-shows",
    #     }
    #     self.client.login(username="testuser", password="testpassword")
    #     response = self.client.post(reverse("create_trip"), data=trip_data)
    # form = TripForm(data=trip_data)
    # self.assertTrue(form.is_valid())
    # self.assertTrue(form.instance.profile)
    # new_trip = Trip.objects.get(id=2)
    # self.assertTrue(Trip.objects.filter(title="West End Shows").exists())

    # self.assertEqual(response.status_code, 302)
    # self.assertRedirects(response,
    #                     reverse_lazy(
    #                         "trip_detail",
    #                         kwargs={
    #                             "slug": self.trip.slug,
    #                             "trip_id": self.trip.id
    #                         }
    #                     )
    #                     )

    def test_trip_update_defensive_programming(self):
        """
        Tests whether a logged in user can access update trip page belonging
        to another user.  It is expected that they should be redirected to the
        403 error template.
        """
        # Login alt user that does not own trip
        self.client.login(username="testuseralt", password="alttestpassword")
        response = self.client.get(
            reverse(
                "update_trip",
                kwargs={"slug": self.trip.slug, "pk": self.trip.id},
            )
        )
        self.assertEqual(response.status_code, 403)

    # def test_get_object_method(self):
    #     """
    #     """
    #     self.client.login(username="testuser", password="testpassword")
    #     response = self.client.get(
    #         reverse(
    #             "update_trip",
    #             kwargs={
    #                 "slug": self.trip.slug,
    #                 "pk": self.trip.id
    #             }
    #         )
    #     )
    #     self.assertTrue(Trip.objects.filter(id=self.trip.id).exists())

    def test_trip_detail(self):
        """ """
        # Login alt user that does not own trip
        self.client.login(username="testuseralt", password="alttestpassword")
        response = self.client.get(
            reverse(
                "trip_detail",
                kwargs={"slug": self.trip.slug, "trip_id": self.trip.id},
            )
        )
        self.assertEqual(response.status_code, 403)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "You can only access your own trips!"
        )

    def test_place_detail_defensive_programming(self):
        """ """
        # Login alt user that does not own trip
        self.client.login(username="testuseralt", password="alttestpassword")
        response = self.client.get(
            reverse(
                "place_detail",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                },
            )
        )
        self.assertEqual(response.status_code, 403)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "This page does not belong to your Trip!"
        )

    def test_trip_delete_defensive_programming(self):
        """
        Tests whether a logged in user can delete a trip belonging to
        another user.  Also tests whether an error message is generated
        if a user attempts to delete a trip that does not belong to them.
        """
        # Login alt user that does not own trip
        self.client.login(username="testuseralt", password="alttestpassword")
        response = self.client.get(
            reverse(
                "delete_trip",
                kwargs={"slug": self.trip.slug, "trip_id": self.trip.id},
            )
        )
        # Checks whether trip still exists
        self.assertTrue(Trip.objects.filter(id=self.trip.id).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "You can only delete your own trips!"
        )

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

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse(
                "review",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                },
            ),
        )

        new_review = Review.objects.get(id=2)
        self.assertEqual(new_review.place, self.place)
        self.assertEqual(new_review.profile, self.profile)
        self.assertEqual(new_review.body, "test review")

    def test_review_create_defensive_programming(self):
        """
        Tests whether a logged in user can access review page belonging
        to another user.  It is expected that they should be redirected to the
        403 error template.
        """
        # Login alt user that does not own trip
        self.client.login(username="testuseralt", password="alttestpassword")
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
        self.assertEqual(response.status_code, 403)

    def test_review_edit_defensive_programming(self):
        """
        Tests whether a logged in user can access review page belonging
        to another user.  It is expected that they should be redirected to the
        403 error template.
        """
        # Login alt user that does not own trip
        self.client.login(username="testuseralt", password="alttestpassword")
        response = self.client.get(
            reverse(
                "edit_review",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                    "review_id": self.review.id,
                },
            )
        )
        self.assertEqual(response.status_code, 403)

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

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "There was an error!")

    def test_review_edit(self):
        """
        Tests edit review
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
                    "review_id": self.review.id,
                },
            ),
            data=review_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse(
                "review",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                },
            ),
        )
        updated_review = Review.objects.get(id=self.review.id)
        self.assertEqual(updated_review.place, self.place)
        self.assertEqual(updated_review.profile, self.profile)
        self.assertEqual(updated_review.body, "update test review")

    def test_invalid_update_review_submission(self):
        """
        Tests response if the review update form submitted is not valid
        """
        self.client.login(username="testuser", password="testpassword")
        review_data = {
            "place": self.place,
            "profile": self.profile,
            "body": "",
        }

        response = self.client.post(
            reverse(
                "edit_review",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                    "review_id": self.review.id,
                },
            ),
            data=review_data,
        )

        # Referenced the following article for testing messages
        # on a response that has no context:
        # https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Error updating this review!")

    def test_review_delete(self):
        """
        Tests Review delete
        """
        self.client.login(username="testuser", password="testpassword")
        review_count = Review.objects.all().count()
        self.assertEqual(review_count, 1)

        response = self.client.get(
            reverse(
                "delete_review",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                    "review_id": self.review.id,
                },
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse(
                "review",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                },
            ),
        )
        self.assertFalse(Review.objects.filter(id=self.review.id).exists())
        updated_review_count = Review.objects.all().count()
        self.assertEqual(updated_review_count, 0)

    def test_review_defensive_programming(self):
        """
        Tests whether a logged in user can delete a review belonging to
        another user.  Also tests whether an error message is generated
        if a user attempts to delete a review that does not belong to them.
        """
        # Login alt user that does not own review
        self.client.login(username="testuseralt", password="alttestpassword")
        response = self.client.get(
            reverse(
                "delete_review",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                    "review_id": self.review.id,
                },
            )
        )
        # Checks whether review still exists
        self.assertTrue(Review.objects.filter(id=self.review.id).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "You can only delete your own reviews!"
        )

    def test_image_delete(self):
        """
        Tests Image delete
        """
        self.client.login(username="testuser", password="testpassword")
        image_count = Image.objects.all().count()
        self.assertEqual(image_count, 1)

        response = self.client.get(
            reverse(
                "delete_image",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                    "image_id": self.image.id,
                },
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse(
                "add_image",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                },
            ),
        )
        self.assertFalse(Image.objects.filter(id=self.image.id).exists())
        updated_image_count = Image.objects.all().count()
        self.assertEqual(updated_image_count, 0)

    def test_add_image_defensive_programming(self):
        """
        Tests whether a logged in user can access add image page belonging
        to another user.  It is expected that they should be redirected to the
        403 error template.
        """
        # Login alt user that does not own trip
        self.client.login(username="testuseralt", password="alttestpassword")
        response = self.client.get(
            reverse(
                "add_image",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                },
            )
        )
        self.assertEqual(response.status_code, 403)

    def test_image_delete_defensive_programming(self):
        """
        Tests whether a logged in user can delete an image belonging to
        another user.  Also tests whether an error message is generated
        if a user attempts to delete an image that does not belong to them.
        """
        # Login alt user that does not own image
        self.client.login(username="testuseralt", password="alttestpassword")
        response = self.client.get(
            reverse(
                "delete_image",
                kwargs={
                    "slug": self.trip.slug,
                    "trip_id": self.trip.id,
                    "place_id": self.place.id,
                    "image_id": self.image.id,
                },
            )
        )
        # Checks whether image still exists
        self.assertTrue(Image.objects.filter(id=self.image.id).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "You can only delete your own images!"
        )
        self.assertEqual(response.status_code, 403)

    def test_successful_trip_delete_redirect(self):
        """ """
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
