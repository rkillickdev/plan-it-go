"""
ORIGINAL GET PLACES THAT MAKES CALL TO APIFY API. REPLACED AS UNRELIABLE IN PRODUCTION
"""


# @staff_member_required
# def get_places(request):
#     """
#     Makes a call to the Apify Trip Advisor Scraper API.  The location
#     submitted by the form is passed to the API and recommended places
#     based on this location are returned.  This response data is then
#     iterated over to filter out any places that are missing necessary
#     fields.
#     A check is then run using the venue_id to see if the place already
#     exists in the database.  If the place does not exist, it is saved
#     as a new instance of Place in the database.
#     """
#     form = PlaceForm
#     requested_location = {}
#     if request.method == 'POST':
#         form = PlaceForm(request.POST)

#         if form.is_valid():
#             requested_location = (form.cleaned_data['location'])

#         # TRY REINSTATING THIS TRY EXCEPT STATEMENT
#         # try:

#         # Initialize the ApifyClient with my API token
#         client = ApifyClient(os.environ.get('MY-APIFY-TOKEN'))

#         # Prepare the Actor input
#         run_input = {
#             "locationFullName": requested_location.city,
#             "maxItems": 40,
#             "language": "en",
#             "currency": "GBP",
#             "includeAttractions": True,
#             "includeHotels": False,
#             "includePriceOffers": False,
#             "includeRestaurants": True,
#             "includeTags": False,
#             "includeVacationRentals": False,
#         }

#         # Run the Actor and wait for it to finish
#         run = client.actor("maxcopell/tripadvisor").call(
#             run_input=run_input
#         )

#         # Fetch Actor results from the run's dataset (if there are any)
#         # Store data as 'places'
#         places = client.dataset(run["defaultDatasetId"]).iterate_items()

#         # Iterates over data retrieved from API call.
#         # Checks if values for certain keys exist.
#         # Returns to top of loop if any of these values are blank.
#         for place in places:
#             required_fields = {
#                 "category": place['category'],
#                 "name": place['name'],
#                 "description": place['description'],
#                 "image": place['image'],
#                 "rating": place['rating'],
#                 "address": place['addressObj'],
#                 "latitude": place['latitude'],
#                 "longitude": place['longitude']
#             }

#             if not all(required_fields.values()):
#                 continue

#             # Creates an instance of Place for each place in the API response.
#             # Populates Place fields with data from API response.
#             place_data = Place(
#                 location=requested_location,
#                 venue_id=place['id'],
#                 type=place['type'],
#                 category=place['category'],
#                 sub_categories=place['subcategories'],
#                 name=place['name'],
#                 location_string=place['locationString'],
#                 description=place['description'],
#                 image=place['image'],
#                 ranking_position=place['rankingPosition'],
#                 rating=place['rating'],
#                 phone=place['phone'],
#                 address=place['addressObj'],
#                 latitude=place['latitude'],
#                 longitude=place['longitude'],
#                 website=place['website'],
#                 ranking_string=place['rankingString'],
#             )

#             # Query database to see if the venue_id used in the API
#             # response already exists. Return to top of loop if it does.
#             venue = Place.objects.filter(
#                 venue_id=place_data.venue_id
#             )

#             # Calculate number of words in description field using numpy
#             word_count = np.char.count(place_data.description, ' ') + 1

#             # Checks if venue already exists of description word count < 50.
#             if venue.exists() or word_count < 30:
#                 continue
#             else:
#                 # Save to database
#                 place_data.save()

#         # retrieved_places = Place.objects.filter(
#         #     location=requested_location.id).order_by('ranking_position')

#         # TRY REINSTATING THIS TRY EXCEPT STATEMENT

#         # except ResponseError as error:
#         #     raise error

#         return HttpResponseRedirect(
#             reverse('place_list', args=[
#                 requested_location.id, requested_location.slug])
#         )

#     else:
#         return render(
#             request, 'places/get_places.html',
#             context={'form': form}
#         )


"""  
This line using Cloudinary to serve static file was removed in favour of using 
whitenoise as per CI Django Blog Webinar.  It goes underneath STATIC URL in
settings.py file.
"""

# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

""" Handy code for checking if any values in a dictionary are empty"""

# if not any(place.values()):



"""
Old Code for Apify API.  If venue already exists, check whether it is
identical to the new version.  I many implement this functionality at a later date.
"""

# if venue.exists():
#                 if venue[0] == place_data:
#                     print(f"Venue id: {place_data.venue_id} already exists and is Identical!")
#                     continue

#             elif place_data.description == "":
#                 print(f"Venue id: {place_data.venue_id} description field was blank") 
#                 continue

#             else:
#                 place_data.save()
#                 print(f'{place_data.name} has been saved')


"""
Old return statement for get_places function if "POST".  It rendered the same page including
form with a list of retrieved places.  I decide it would be better to redirect to the place_list page
to display all the retrievd places.
"""

# context = {
        #     'form': form,
        #     'retrieved_places': retrieved_places,
        # }

        # return render(request, 'places/get_places.html', context)


"""
This was the code I wrote initially when I planned to not have a separate detail
page for each recommendation.  In the end I decided against this.
"""

# class TripRecommendationsView(LoginRequiredMixin, View):
#     """
#     View to render recommended places to visit based on the trip location.
#     A query is made on the Place model to find all places that
#     have a location field that matches the trip location attribute.
#     This queryset is stored in the context dictionary as 'places'so it can be
#     accessed by the trip_recommendations.html template.
#     """

#     def get(self, request, slug, pk, *args, **kwargs):
#         # Queryset filtered to only contain trips belonging to logged in user
#         queryset = Trip.objects.filter(profile=request.user.profile.id)

#         trip = get_object_or_404(queryset, id=pk)
#         places = Place.objects.filter(location=trip.location).order_by(
#             'ranking_position')

#         # Creates a queryset of reviews for all the listed places
#         # The following stack overflow article was used to find a solution to this:
#         # https://stackoverflow.com/questions/47236667/django-combine-multiple-querysets-same-model
#         reviews = Review.objects.all()
#         q = Q()
#         for place in places:
#             q = q | Q(approved=True)
#         reviews.filter(q)

#         return render(
#             request,
#             'trips/trip_recommendations.html',
#             {
#                 'trip': trip,
#                 'places': places,
#                 'reviews': reviews,
#                 'review_form': ReviewForm()
#             }

#         )

#     def post(self, request, slug, pk, *args, **kwargs):
#         # Queryset filtered to only contain trips belonging to logged in user
#         queryset = Trip.objects.filter(profile=request.user.profile.id)

#         trip = get_object_or_404(queryset, id=pk)
#         places = Place.objects.filter(location=trip.location).order_by(
#             'ranking_position')

#         # Creates a queryset of reviews for all the listed places
#         # The following stack overflow article was used to find a solution to this:
#         # https://stackoverflow.com/questions/47236667/django-combine-multiple-querysets-same-model
#         reviews = Review.objects.all()
#         q = Q()
#         for place in places:
#             q = q | Q(approved=True)
#         reviews.filter(q)

#         review_form = ReviewForm(data=request.POST)

#         if review_form.is_valid():
#             review_form.instance.place = place
#             review_form.instance.profile = request.user.profile

#         return render(
#             request,
#             'trips/trip_recommendations.html',
#             {
#                 'trip': trip,
#                 'places': places,
#                 'reviews': reviews,
#                 'review_form': ReviewForm()
#             }

#         )

# LONGER VERSION OF PLACES DETAIL VIEW WHEN IT WAS ORIGINALLY NECESSARY
# TO INCLUDEW THE REVIEW FORM ON THIS PAGE.  IT HAS SINCE BEEN MOVED TO ITS OWN
# REVIEW PAGE.

# @login_required()
# def place_detail(request, slug, trip_id, place_id, *args, **kwargs):
#     """
#     A function based view to render specific details of a recommended place
#     to the recommended_detail.html template.  The specific place is passed
#     as an object to the template as part of the context, along the with a
#     queryset of all reviews relating to the place and the review form.
#     The trip object is included so places can be added or removed from the
#     trip itinerary.
#     """

#     trip = get_object_or_404(Trip, id=trip_id)
#     place = get_object_or_404(Place, id=place_id)
#     reviews = place.reviews.all().order_by('created_on')
#     images = place.images.all().order_by('created_on')
#     added = False

#     if trip.places.filter(id=place.id).exists():
#         added = True

#     if request.method == "POST":
#         review_form = ReviewForm(data=request.POST)
#         if review_form.is_valid():
#             review_form.instance.profile = request.user.profile
#             review = review_form.save(commit=False)
#             review.place = place
#             review.save()
#             messages.add_message(request, messages.SUCCESS, 'Review Complete!')

#         else:
#             review_form = ReviewForm()
#             messages.add_message(
#                 request, messages.ERROR, 'There was an error!'
#             )
#     else:
#         review_form = ReviewForm()

#     return render(
#         request,
#         'trips/place_detail.html',
#         {
#             'trip': trip,
#             'place': place,
#             'added': added,
#             'reviews': reviews,
#             'images': images,
#             'review_form': ReviewForm()
#         }
#     )

# TRIP RECOMMENDATION FUNCTIONALITY ROLED INTO TRIP DETAIL VIEW

# class TripRecommendationsView(LoginRequiredMixin, View):
#     """
#     View to render recommended places to visit based on the trip location.
#     A query is made on the Place model to find all places that
#     have a location field that matches the trip location attribute.
#     This queryset is stored in the context dictionary as 'places'so it can be
#     accessed by the trip_recommendations.html template.
#     """

#     def get(self, request, slug, trip_id, *args, **kwargs):

#         trip = get_object_or_404(Trip, id=trip_id)
#         places = Place.objects.filter(location=trip.location).order_by(
#             'ranking_position')

#         return render(
#             request,
#             'trips/trip_recommendations.html',
#             {
#                 'trip': trip,
#                 'places': places
#             }

#         )


"""
BELOW ARE 2 WAYS TO DELETE LOCATION.  DECIDED AGAINST THIS OPTION AS THE KNOCK
ON WOULD BE THAT ALL ASSOCIATED PLACES AND TRIPS WOULD ALSO BE DELETED!
"""

# @login_required()
# def delete_destination(request, location_id, *args, **kwargs):
#     location = get_object_or_404(Location, id=location_id)

#     location.delete()

#     if image.profile.id == request.user.profile.id:
#         location.delete()
#         messages.add_message(request, messages.SUCCESS, 'Image deleted!')
#     else:
#         messages.add_message(request, messages.ERROR, 'You can only delete your own images!')

#     return HttpResponseRedirect(
#         reverse('locations')
#     )


# class DeleteDestination(LoginRequiredMixin, DeleteView):

#     form_class = LocationForm
#     model = Location
#     template_name = 'locations/destinations.html'

#     def get_context_data(self, **kwargs):
#         context = super(DeleteDestination, self).get_context_data(**kwargs)
#         context['destinations'] = Location.objects.all().order_by('city')
#         return context

#     def get_success_url(self):
#         return reverse_lazy('locations')

# EXPERIMENTING WITH WAYS TO RENDER REVIEW PAGE




# THIS WAD ORIGINALLY PART OF THE TRIP DETAIL CLASS BASED VIEW.
# REMOVED AS NO LONGER REQUIRED POST METHOD

# def post(self, request, slug, trip_id, place_id, *args, **kwargs):

    #     trip = get_object_or_404(Trip, id=trip_id)
    #     place = get_object_or_404(Place, id=place_id)

    #     review_form = ReviewForm(data=request.POST)

    #     if review_form.is_valid():
    #         review_form.instance.profile = request.user.profile
    #         review = review_form.save(commit=False)
    #         review.place = place
    #         review.save()
    #         messages.add_message(request, messages.SUCCESS, 'Review Complete!')

    #     else:
    #         review_form = ReviewForm()
    #         messages.add_message(
    #             request, messages.ERROR, 'There was an error!'
    #         )

    #     return render(
    #             request,
    #             'trips/trip_detail.html',
    #             {
    #                 'trip': trip,
    #                 'review_form': ReviewForm()
    #             }

    #         )