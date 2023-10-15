from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Location
from .forms import LocationForm


class DestinationList(LoginRequiredMixin, CreateView):
    """
    View where a logged in user can upload an image to the gallery page.
    Once successfully uploaded, the user is redirected back to the same page
    where the newly uploaded image is displayed along side all other images
    for the specified place.
    The URL parameters passed into the view are accessed from the kwargs.
    A queryset of images and the specific places object is made avaialble 
    as part of the context when rendering  the template, by defining the 
    get_context_data() method.
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
        return reverse_lazy('add_image')
