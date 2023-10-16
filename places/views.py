from django.shortcuts import render
from django.shortcuts import get_object_or_404
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
            'ranking_position')


class PlaceBrowseDetail(DetailView):
    """
    View to used to render details of a place for staff and users
    that have not signed in.
    """

    model = Place
    template_name = 'places/browse_detail.html'


@staff_member_required
def get_places(request):
    form = PlaceForm
    requested_location = {}
    if request.method == 'POST':
        form = PlaceForm(request.POST)

        if form.is_valid():
            requested_location = (form.cleaned_data['location'])

        # TRY REINSTATING THIS TRY EXCEPT STATEMENT
        # try:

        # Initialize the ApifyClient with my API token
        client = ApifyClient(os.environ.get('MY-APIFY-TOKEN'))

        # Prepare the Actor input
        run_input = {
            "locationFullName": requested_location.city,
            "maxItems": 5,
            "language": "en",
            "currency": "GBP",
            "includeAttractions": True,
            "includeHotels": False,
            "includePriceOffers": False,
            "includeRestaurants": True,
            "includeTags": False,
            "includeVacationRentals": False,
        }

        # Run the Actor and wait for it to finish
        run = client.actor("maxcopell/tripadvisor").call(
            run_input=run_input
        )

        # Fetch Actor results from the run's dataset (if there are any)
        # Store data as 'places'
        places = client.dataset(run["defaultDatasetId"]).iterate_items()

        # Iterates over data retrieved from API call.
        # Creates an instance of Place for each place in the API response.
        # Populates Place fields with data from API response.
        for place in places:
            if not place['description'] or not place['image'] or not place['name'] or not place['address'] or not place['latitude'] or not place['longitude']:
                print("skipped this one")
                continue
            print(place)
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
            # response already exists.
            venue = Place.objects.filter(
                venue_id=place_data.venue_id
            )

            if venue.exists():
                if venue[0] == place_data:
                    #  and venue[0].ranking_position == place_data.ranking_position:
                    print(f"Venue id: {place_data.venue_id} already exists and is Identical!")
                    continue

            elif place_data.description == "":
                print(f"Venue id: {place_data.venue_id} description field was blank") 
                continue

            else:
                place_data.save()
                print(f'{place_data.name} has been saved')

        retrieved_places = Place.objects.filter(location=requested_location.id).order_by('ranking_position')

        context = {
            'form': form,
            'retrieved_places': retrieved_places,
        }

        # TRY REINSTATING THIS TRY EXCEPT STATEMENT

        # except ResponseError as error:
        #     raise error

        return render(request, 'places/get_places.html', context)

    else:
        return render(
            request, 'places/get_places.html',
            context={'form': form}
        )
