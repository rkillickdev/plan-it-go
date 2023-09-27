from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    """

    """
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
    def get(self, request, slug, trip_id, *args, **kwargs):

        trip = get_object_or_404(Trip, id=trip_id)

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

    def get(self, request, slug, trip_id, *args, **kwargs):

        trip = get_object_or_404(Trip, id=trip_id)
        places = Place.objects.filter(location=trip.location).order_by(
            'ranking_position')

        return render(
            request,
            'trips/trip_recommendations.html',
            {
                'trip': trip,
                'places': places
            }

        )


@login_required()
def place_detail(request, slug, trip_id, place_id, *args, **kwargs):
    """
    A function based view to render specific details of a recommended place
    to the recommended_detail.html template.  The specific place is passed
    as an object to the template as part of the context, along the with a
    queryset of all reviews relating to the place and the review form.
    The trip object is included so places can be added or removed from the
    trip itinerary.
    """

    trip = get_object_or_404(Trip, id=trip_id)
    place = get_object_or_404(Place, id=place_id)
    reviews = place.reviews.all().order_by('created_on')

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.profile = request.user.profile
            review = review_form.save(commit=False)
            review.place = place
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Complete!')

        else:
            review_form = ReviewForm()
            messages.add_message(
                request, messages.ERROR, 'There was an error!'
            )
    else:
        review_form = ReviewForm()

    return render(
        request,
        'trips/recommended_detail.html',
        {
            'trip': trip,
            'place': place,
            'reviews': reviews,
            'review_form': ReviewForm()
        }
    )


def review_edit(request, trip_id, place_id, review_id, *args, **kwargs):

    if request.method == "POST":
        trip = get_object_or_404(Trip, id=trip_id)
        place = get_object_or_404(Place, id=place_id)
        review = get_object_or_404(Review, id=review_id)

        review_form = ReviewForm(data=request.POST, instance=review)
        if review_form.is_valid() and review.profile.id == request.user.profile.id:
            review = review_form.save(commit=False)
            review.place = place
            review.approved = False
            review.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment Updated!'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    return HttpResponseRedirect(
        reverse('place_detail', args=[trip.slug, trip_id, place_id])
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
