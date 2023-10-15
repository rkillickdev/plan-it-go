from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Location
from .forms import LocationForm


class DestinationList(LoginRequiredMixin, CreateView):
    """
    """

    form_class = LocationForm
    model = Location
    template_name = 'locations/destinations.html'

    # Referenced this article to find out about modifying context data
    # in a class based view:
    # https://magbanum.com/blog/let-cloudinary-handle-image-uploads-in-your-django-application

    def get_context_data(self, **kwargs):
        context = super(DestinationList, self).get_context_data(**kwargs)
        context['destinations'] = Location.objects.all().order_by('city')
        return context

    def get_success_url(self):
        return reverse_lazy('locations')
