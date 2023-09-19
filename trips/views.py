from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, ListView,
    DetailView, UpdateView, DeleteView
)
from .models import Trip
from .models import Profile
from .forms import TripForm


class TripCreateView(CreateView):
    """
    View to render the profile update form.
    """
    form_class = TripForm
    model = Trip
    success_url = reverse_lazy('trip_list')

    # Populate profile field of the model Trip with the profile linked to the
    # logged in user.
    # https://stackoverflow.com/questions/18246326/how-do-i-set-user-field-in-form-to-the-currently-logged-in-user
    def form_valid(self, form):
        form.instance.profile = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


class TripListView(ListView):
    model = Trip
    context_object_name = "trip_list"
