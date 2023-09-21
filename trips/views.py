from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, ListView,
    DetailView, UpdateView, DeleteView
)
from .models import Trip
from .models import Profile
from .forms import TripForm


class TripCreateView(LoginRequiredMixin, CreateView):
    """
    View to render the profile update form.
    """
    form_class = TripForm
    model = Trip

    # Assign slug field for the location of the trip to the success url
    # The following stack overflow helped with understanding self.object:
    # https://stackoverflow.com/questions/52063861/django-access-form-argument-in-createview-to-pass-to-get-success-url
    def get_success_url(self):
        return reverse_lazy(
            'place_list',
            kwargs={'slug': self.object.location.slug}
        )

    """
    Populate profile field of the model Trip with the profile linked to the
    logged in user.
    https://stackoverflow.com/questions/18246326/how-do-i-set-user-field-in-form-to-the-currently-logged-in-user
    """
    def form_valid(self, form):
        form.instance.profile = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


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


class TripDetailView(LoginRequiredMixin, DetailView):
    """
    View to render details of a specific trip
    """
    model = Trip
