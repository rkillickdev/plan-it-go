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