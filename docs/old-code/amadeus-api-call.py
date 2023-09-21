from django.shortcuts import render
from amadeus import Client, ResponseError
from .forms import PlaceForm
from .models import Place

import os
if os.path.isfile('env.py'):
    import env


def get_places(request):
    form = PlaceForm
    requested_location = {}
    if request.method == 'POST':
        form = PlaceForm(request.POST)

        if form.is_valid():
            requested_location = (form.cleaned_data['location'])

        amadeus = Client(
            client_id=os.environ.get('AMADEUS_API_KEY'),
            client_secret=os.environ.get('AMADEUS_API_SECRET')
        )

        try:
            """
            Makes call to Amadeus API to retrieve points of interest.
            Argument passed to the API are latitude and longitude which
            are attributes of the Location object submitted by the
            PlaceForm.
            """
            response = (
                amadeus.reference_data.locations.points_of_interest.get(
                    latitude=requested_location.latitude,
                    longitude=requested_location.longitude
                )
            )
            places = response.data

            # Iterates over data retrieved from API call.
            # Creates an instance of Place for each place in the API response.
            # Populates Place fields with data from API response.
            for place in places:
                place_data = Place(
                    location=requested_location,
                    venue_id=place['id'],
                    name=place['name'],
                    latitude=place['geoCode']['latitude'],
                    longitude=place['geoCode']['longitude'],
                    category=place['category'],
                    rank=place['rank'],
                    tags=place['tags'],
                )

                # Query database to see if the venue_id used in the API
                # response already exists.
                venue = Place.objects.filter(
                    venue_id=place_data.venue_id
                )
                if venue.exists() and venue[0].rank == place_data.rank:
                    print(f"Venue id: {place_data.venue_id} Already Exists")
                else:
                    place_data.save()
                    print(f'{place_data.name} has been saved')

                all_places = Place.objects.all().order_by('rank')

            context = {
                'form': form,
                'all_places': all_places,
            }

        except ResponseError as error:
            raise error

        return render(request, 'places/get_places.html', context)

    else:
        return render(
            request, 'places/get_places.html',
            context={'form': form}
        )