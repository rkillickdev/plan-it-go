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