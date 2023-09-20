from django.shortcuts import render
from django.urls import reverse
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
            print(requested_location.summary)

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
            context = {
                'form': form,
                'places': places,
            }
            print(places)

        except ResponseError as error:
            raise error

        return render(request, 'places/get_places.html', context)

    else:
        return render(
            request, 'places/get_places.html',
            context={'form': form}
        )
