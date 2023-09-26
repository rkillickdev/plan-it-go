from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView, ListView,
    DetailView, UpdateView, DeleteView
)
from .models import Trip
from .models import Profile
from .models import Place
from places.models import Review
from .forms import TripForm
from places.forms import ReviewForm


class TripCreateView(LoginRequiredMixin, CreateView):
    """
    View to render the profile update form.
    Assigns slug field and primary key id to kwargs.
    The get_success_url() method is used to redirect to 'get_detail.html'.
    The following stack overflow helped with understanding self.object:
    https://stackoverflow.com/questions/52063861/django-access-form-argument-in-createview-to-pass-to-get-success-url
    """
    form_class = TripForm
    model = Trip

    def get_success_url(self):
        return reverse_lazy(
            'trip_detail',
            kwargs={
                'slug': self.object.slug,
                'pk': self.object.id
            }
        )

    """
    Populate profile field of the model Trip with the profile linked to the
    logged in user.
    https://stackoverflow.com/questions/18246326/how-do-i-set-user-field-in-form-to-the-currently-logged-in-user
    """
    def form_valid(self, form):
        form.instance.profile = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


class TripUpdateView(LoginRequiredMixin, UpdateView):
    model = Trip
    form_class = TripForm

    def get_success_url(self):
        return reverse_lazy(
            'trip_detail',
            kwargs={
                'slug': self.object.slug,
                'pk': self.object.id
            }
        )


class TripListView(LoginRequiredMixin, ListView):
    """
    View to render a list of trips linked to the profile of the logged in user
    """
    model = Trip
    context_object_name = "trip_list"

    """
    Filters queryset so only trips linked to the profile of the logged in
    user are available to view.
    Referenced this article when investigating how to achieve this:
    https://stackoverflow.com/questions/59408167/list-of-current-user-objects-in-django-listview
    """
    def get_queryset(self):
        return Trip.objects.filter(
            profile=self.request.user.profile
        ).order_by('-start_date')


class TripDetailView(LoginRequiredMixin, View):
    """
    View to render details of a specific trip, including an itinerary of
    places to visit, created by the user.  The get() method receives both
    a slug and pk in the url.  The slug is included to make the url more
    informative to the user.  The pk is used to look up the requested trip
    object using get_object_or_404().  This object is then included in the
    context dictionary as 'trip' so it can be accessed by the trip_detail.html
    file.
    """
    def get(self, request, slug, pk, *args, **kwargs):
        # Queryset filtered to only contain trips belonging to logged in user
        queryset = Trip.objects.filter(profile=request.user.profile.id)

        trip = get_object_or_404(queryset, id=pk)

        return render(
            request,
            'trips/trip_detail.html',
            {
                'trip': trip,
            }

        )


class TripRecommendationsView(LoginRequiredMixin, View):
    """
    View to render recommended places to visit based on the trip location.
    A query is made on the Place model to find all places that
    have a location field that matches the trip location attribute.
    This queryset is stored in the context dictionary as 'places'so it can be
    accessed by the trip_recommendations.html template.
    """

    def get(self, request, slug, pk, *args, **kwargs):
        # Queryset filtered to only contain trips belonging to logged in user
        queryset = Trip.objects.filter(profile=request.user.profile.id)

        trip = get_object_or_404(queryset, id=pk)
        places = Place.objects.filter(location=trip.location).order_by(
            'ranking_position')

        # Creates a queryset of reviews for all the listed places
        # The following stack overflow article was used to find a solution to this:
        # https://stackoverflow.com/questions/47236667/django-combine-multiple-querysets-same-model
        reviews = Review.objects.all()
        q = Q()
        for place in places:
            q = q | Q(approved=True)
        reviews.filter(q)
        print(reviews)

        return render(
            request,
            'trips/trip_recommendations.html',
            {
                'trip': trip,
                'places': places,
                'reviews': reviews,
                'review_form': ReviewForm()
            }

        )


class PlaceAdd(LoginRequiredMixin, View):

    def post(self, request, trip_id, place_id):
        trip = get_object_or_404(Trip, id=trip_id)
        place = get_object_or_404(Place, id=place_id)

        if trip.places.filter(id=place.id).exists():
            trip.places.remove(place)
        else:
            trip.places.add(place)

        return HttpResponseRedirect(
            reverse('trip_recommendations', args=[trip.slug, trip_id]))
