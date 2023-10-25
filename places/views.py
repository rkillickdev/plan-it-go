import numpy as np
import json

from django.contrib import messages
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from apify_client import ApifyClient
from .forms import PlaceForm
from .models import Place
from .models import Location

import os
if os.path.isfile('env.py'):
    import env


class PlaceListView(ListView):
    """
    View to render a list of places based on the trip location
    """

    model = Place
    context_object_name = "places"
    paginate_by = 6

    def get_queryset(self):
        self.location = get_object_or_404(
            Location, id=self.kwargs['location_id'])
        return Place.objects.filter(location=self.location).order_by(
            'rating')


class PlaceBrowseDetail(DetailView):
    """
    View to used to render details of a place for staff and users
    that have not signed in.
    """

    model = Place
    template_name = 'places/browse_detail.html'


@staff_member_required
def get_places(request):
    """
    The location submitted by the form is slugified and .json appended
    to the end of the string to match the formatting of stored json files.
    If the resulting file path can be found, the corresponding json file
    is parsed and stored in the variable called python_data.
    The variable python_data is then iterated over to check a dictionary of
    required_fields.  If values do not exist for these fields, the loop
    restarts and checks the next place.
    A check is then run using the venue_id to see if the place already
    exists in the database or if the description word count is less than 30.  
    If the place does not already exist and word count greater than 30, it 
    is saved as a new instance of Place in the database.
    """

    # Retrieve location name from submitted form
    form = PlaceForm
    requested_location = {}
    if request.method == 'POST':
        form = PlaceForm(request.POST)

        if form.is_valid():
            requested_location = (form.cleaned_data['location'])
            # format location to insert in file path request
            location_file = slugify(requested_location) + ".json"

        try:
            # Try to open and read requested file
            with open(f"static/data/{location_file}", 'r') as apify_file:
                apify_data = apify_file.read()

        except Exception as error:
            # Alert user ff requested file cannot be found
            messages.add_message(
                request, messages.ERROR, 'We were not able to retrieve this data!'
            )

        # Parse json file
        python_data = json.loads(apify_data)

        # Iterates over data retrieved from json file.
        # Checks if values for certain keys exist.
        # Returns to top of loop if any of these values are blank.
        for place in python_data:
            required_fields = {
                "category": place['category'],
                "name": place['name'],
                "description": place['description'],
                "image": place['image'],
                "rating": place['rating'],
                "address": place['addressObj'],
                "latitude": place['latitude'],
                "longitude": place['longitude']
            }

            if not all(required_fields.values()):
                continue

            # Creates an instance of Place for each place in the json file.
            # Populates Place fields with data from API response.
            place_data = Place(
                location=requested_location,
                venue_id=place['id'],
                type=place['type'],
                category=place['category'],
                sub_categories=place['subcategories'],
                name=place['name'],
                location_string=place['locationString'],
                description=place['description'],
                image=place['image'],
                ranking_position=place['rankingPosition'],
                rating=place['rating'],
                phone=place['phone'],
                address=place['addressObj'],
                latitude=place['latitude'],
                longitude=place['longitude'],
                website=place['website'],
                ranking_string=place['rankingString'],
            )

            # Query database to see if the venue_id used in the API
            # response already exists. Return to top of loop if it does.
            venue = Place.objects.filter(
                venue_id=place_data.venue_id
            )

            # Calculate number of words in description field using numpy
            word_count = np.char.count(place_data.description, ' ') + 1

            # Checks if venue already exists of description word count < 30.
            if venue.exists() or word_count < 30:
                continue
            else:
                # Save to database
                place_data.save()

        return HttpResponseRedirect(
            reverse('place_list', args=[
                requested_location.id, requested_location.slug])
        )

    else:
        return render(
            request, 'places/get_places.html',
            context={'form': form}
        )
