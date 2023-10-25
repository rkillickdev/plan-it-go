"""
ORIGINAL GET PLACES THAT MAKES CALL TO APIFY API. REPLACED AS UNRELIABLE IN PRODUCTION
"""

@staff_member_required
def get_places(request):
    """
    Makes a call to the Apify Trip Advisor Scraper API.  The location
    submitted by the form is passed to the API and recommended places
    based on this location are returned.  This response data is then
    iterated over to filter out any places that are missing necessary
    fields.
    A check is then run using the venue_id to see if the place already
    exists in the database.  If the place does not exist, it is saved
    as a new instance of Place in the database.
    """
    form = PlaceForm
    requested_location = {}
    if request.method == 'POST':
        form = PlaceForm(request.POST)

        if form.is_valid():
            requested_location = (form.cleaned_data['location'])

        # Initialize the ApifyClient with my API token
        client = ApifyClient(os.environ.get('MY-APIFY-TOKEN'))

        # Prepare the Actor input
        run_input = {
            "locationFullName": requested_location.city,
            "maxItems": 40,
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
        # Checks if values for certain keys exist.
        # Returns to top of loop if any of these values are blank.
        for place in places:
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

            # Creates an instance of Place for each place in the API response.
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

            # Checks if venue already exists of description word count < 50.
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
