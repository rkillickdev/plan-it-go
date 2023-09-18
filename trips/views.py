from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, ListView,
    DetailView, UpdateView, DeleteView
)
from .models import Trip
from .forms import TripForm


class TripCreateView(CreateView):
    """
    View to render the profile update form.
    """
    form_class = TripForm
    model = Trip
    success_url = reverse_lazy('trip_list')


class TripListView(ListView):
    model = Trip
    context_object_name = "trip_list"
