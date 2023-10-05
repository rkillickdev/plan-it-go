# # This was the code I wrote initially when I planned to not have a separate detail
# # page for each recommendation.  In the end I decided against this.

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


# EXPERIMENTING WITH WAYS TO RENDER REVIEW PAGE

# @login_required()
# def review(request, slug, trip_id, place_id, *args, **kwargs):

#     trip = get_object_or_404(Trip, id=trip_id)
#     place = get_object_or_404(Place, id=place_id)
#     reviews = place.reviews.all().order_by('created_on')

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
#             request,
#             'trips/review.html',
#             {
#                 'trip': trip,
#                 'place': place,
#                 'reviews': reviews,
#                 'review_form': ReviewForm()
#             }

#         )


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