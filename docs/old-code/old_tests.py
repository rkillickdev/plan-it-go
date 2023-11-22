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

"""
Experimentation in trips view.py test file.  To be continued
"""

def test_successful_trip_create_form_valid(self):
        form_data = {
            # 'profile': self.profile,
            'location': self.location,
            'title': 'The Bright Lights',
            'slug': 'the-bright-lights',
            'description': 'about the trip'
        }
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("create_trip"))
        form = TripForm(form_data)
        self.assertTrue(form.instance.profile)
        self.assertTrue(form.is_valid())

def test_get_success_url_redirect(self):
    """
    """
    trip_data = {
        "profile": self.profile,
        "location": self.location,
        "title": "West End Shows",
        "slug": "west-end-shows",
    }
    self.client.login(username="testuser", password="testpassword")
    response = self.client.post(reverse("create_trip"), data=trip_data)
form = TripForm(data=trip_data)
self.assertTrue(form.is_valid())
self.assertTrue(form.instance.profile)
new_trip = Trip.objects.get(id=2)
self.assertTrue(Trip.objects.filter(title="West End Shows").exists())

self.assertEqual(response.status_code, 302)
self.assertRedirects(response,
                    reverse_lazy(
                        "trip_detail",
                        kwargs={
                            "slug": self.trip.slug,
                            "trip_id": self.trip.id
                        }
                    )
                    )

def test_get_object_method(self):
    """
    """
    self.client.login(username="testuser", password="testpassword")
    response = self.client.get(
        reverse(
            "update_trip",
            kwargs={
                "slug": self.trip.slug,
                "pk": self.trip.id
            }
        )
    )
    self.assertTrue(Trip.objects.filter(id=self.trip.id).exists())

# This was part of test_successful_trip_delete_redirect.  An experiment

url = reverse('create_trip')
request = self.factory.get(url)
view = TripCreateView()
view.setup(request)
request.user = self.user
response = TripCreateView.as_view()(request)
self.assertEqual(response.status_code, 200)

"""Experimenting ends here"""