from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import Location
from .forms import LocationForm


class CreateDestination(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View to create a destination.  A success message has been added on
    successful creation.  Destinations ordered by the city field are
    returned as the view context.
    """

    form_class = LocationForm
    model = Location
    template_name = "locations/destinations.html"
    success_message = "Congratulations, you created a new destination!"

    # Referenced this article to find out about modifying context data
    # in a class based view:
    # https://magbanum.com/blog/let-cloudinary-handle-image-uploads-in-your-django-application

    def get_context_data(self, **kwargs):
        context = super(CreateDestination, self).get_context_data(**kwargs)
        context["destinations"] = Location.objects.all().order_by("city")
        return context

    def get_success_url(self):
        return reverse_lazy("locations")


class UpdateDestination(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View to update a destination.  A success message has been added on
    successful update.  Destinations ordered by the city field are
    returned as the view context.
    """

    form_class = LocationForm
    model = Location
    template_name = "locations/destinations.html"
    success_message = "You have successfully updated a destination"

    def get_context_data(self, **kwargs):
        context = super(UpdateDestination, self).get_context_data(**kwargs)
        context["destinations"] = Location.objects.all().order_by("city")
        return context

    def get_success_url(self):
        return reverse_lazy("locations")
