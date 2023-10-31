import os
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView, ListView,
    DetailView, UpdateView, DeleteView
)
from .models import Trip, Profile, Place, Location
from places.models import Review, Image
from .forms import TripForm
from places.forms import ReviewForm, ImageForm


class TripBrowse(ListView):
    """
    View to render a list of trips based on the location id argument
    supplied in the url.
    """

    model = Trip
    context_object_name = "destination_trips"
    template_name = 'trips/trip_browse.html'

    def get_queryset(self):
        self.location = get_object_or_404(Location, id=self.kwargs['location_id'])
        return Trip.objects.filter(location=self.location).order_by(
            'created_on')


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
    template_name = 'trips/create_trip.html'

    def get_success_url(self):
        return reverse_lazy(
            'trip_detail',
            kwargs={
                'slug': self.object.slug,
                'trip_id': self.object.id
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
    template_name = 'trips/create_trip.html'

    def get_success_url(self):
        return reverse_lazy(
            'trip_detail',
            kwargs={
                'slug': self.object.slug,
                'trip_id': self.object.id
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
    Also included in the context dictionary is 'places'.  This is a filtered
    queryset of all places relating to the location of the trip, that have
    NOT already been added to the 'places' many to many field of the trip.
    These places are then displayed as recommendations in the trip_detail.html 
    template.
    """
    def get(self, request, slug, trip_id, *args, **kwargs):

        trip = get_object_or_404(Trip, id=trip_id)
        geo_data = list(Place.objects.filter(id__in=trip.places.values_list(
            'id', flat=True)).values('latitude', 'longitude'))

        geo_list = []

        # Prepares list of geo data named correctly to pass to Google Maps
        for item in geo_data:
            new_dict = {'lat': float(item['latitude']), 'lng': float(
                item['longitude'])}
            geo_list.append(new_dict)

        # Used the following tutorial to help with pagination for function based views:
        # https://www.youtube.com/watch?v=N-PB-HMFmdo&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=18
        p = Paginator(Place.objects.filter(location=trip.location).exclude(
            id__in=trip.places.values_list('id', flat=True)).order_by(
                'ranking_position'
            ), 3)
        page = request.GET.get('page')
        places = p.get_page(page)

        g_maps_api_key = os.environ.get('GOOGLE_MAPS_API_KEY')

        return render(
            request,
            'trips/trip_detail.html',
            {
                'trip': trip,
                'places': places,
                'g_maps_api_key': g_maps_api_key,
                'geo_list': geo_list
            }

        )


class PlaceDetail(LoginRequiredMixin, View):
    """
    A function based view to render specific details of a recommended place
    to the recommended_detail.html template.  The specific place is passed
    as an object to the template as part of the context, along the with a
    queryset of all reviews relating to the place and the review form.
    The trip object is included so places can be added or removed from the
    trip itinerary.
    """
    def get(self, request, slug, trip_id, place_id, *args, **kwargs):

        trip = get_object_or_404(Trip, id=trip_id)
        place = get_object_or_404(Place, id=place_id)
        reviews = place.reviews.filter(approved=True).order_by('created_on')
        images = place.images.filter(approved=True).order_by('created_on')
        added = False

        if trip.places.filter(id=place.id).exists():
            added = True

        g_maps_api_key = os.environ.get('GOOGLE_MAPS_API_KEY')

        return render(
            request,
            'trips/place_detail.html',
            {
                'trip': trip,
                'place': place,
                'added': added,
                'reviews': reviews,
                'images': images,
                'g_maps_api_key': g_maps_api_key

            }
        )


@login_required()
def review_create(request, slug, trip_id, place_id, *args, **kwargs):

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
            'trips/review.html',
            {
                'trip': trip,
                'place': place,
                'reviews': reviews,
                'review_form': ReviewForm()
            }

        )


# class CreateReview(LoginRequiredMixin, View):
#     """
#     """

#     def get(self, request, slug, trip_id, place_id, *args, **kwargs):
#         trip = get_object_or_404(Trip, id=trip_id)
#         place = get_object_or_404(Place, id=place_id)
#         reviews = place.reviews.all().order_by('created_on')

#         return render(
#                 request,
#                 'trips/review.html',
#                 {
#                     'trip': trip,
#                     'place': place,
#                     'reviews': reviews,
#                     'review_form': ReviewForm()
#                 }

#             )


@login_required()
def review_edit(request, trip_id, place_id, review_id, *args, **kwargs):
    """
    """
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
        reverse('review', args=[trip.slug, trip_id, place_id])
    )


@login_required()
def review_delete(request, trip_id, place_id, review_id, *args, **kwargs):
    """
    """

    trip = get_object_or_404(Trip, id=trip_id)
    place = get_object_or_404(Place, id=place_id)
    review = get_object_or_404(Review, id=review_id)

    if review.profile.id == request.user.profile.id:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(
        reverse('review', args=[trip.slug, trip_id, place_id])
    )


class ImageUploadView(LoginRequiredMixin, CreateView):
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

    form_class = ImageForm
    model = Image
    template_name = 'trips/add_image.html'

    # Referenced this article to find out about accessing url kwargs:
    # https://stackoverflow.com/questions/72599545/get-url-kwargs-in-class-based-views

    def setup(self, request, *args, **kwargs):
        self.place_id = kwargs['place_id']
        self.trip_id = kwargs['trip_id']
        return super().setup(request, *args, **kwargs)

    # Referenced this article to automatically populate filed forms:
    # https://stackoverflow.com/questions/18246326/how-do-i-set-user-field-in-form-to-the-currently-logged-in-user

    def form_valid(self, form):
        image = form.save(commit=False)
        image.profile = Profile.objects.get(user=self.request.user)
        image.place = get_object_or_404(Place, id=self.place_id)
        image.save()
        return HttpResponseRedirect(self.get_success_url())

    # Referenced this article to find out about modifying context data
    # in a class based view:
    # https://magbanum.com/blog/let-cloudinary-handle-image-uploads-in-your-django-application

    def get_context_data(self, **kwargs):
        context = super(ImageUploadView, self).get_context_data(**kwargs)
        context['images'] = Image.objects.filter(profile=self.request.user.profile.id).order_by('created_on')
        context['place'] = get_object_or_404(Place, id=self.kwargs['place_id'])
        context['trip'] = get_object_or_404(Trip, id=self.kwargs['trip_id'])
        return context

    def get_success_url(self):
        return reverse_lazy(
            'add_image',
            kwargs={
                'slug': self.kwargs['slug'],
                'trip_id': self.kwargs['trip_id'],
                'place_id': self.kwargs['place_id']
            }
        )


@login_required()
def image_delete(request, trip_id, place_id, image_id, *args, **kwargs):
    trip = get_object_or_404(Trip, id=trip_id)
    place = get_object_or_404(Place, id=place_id)
    image = get_object_or_404(Image, id=image_id)

    if image.profile.id == request.user.profile.id:
        image.delete()
        messages.add_message(request, messages.SUCCESS, 'Image deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own images!')

    return HttpResponseRedirect(
        reverse('add_image', args=[trip.slug, trip_id, place_id])
    )


class PlaceToggle(LoginRequiredMixin, View):

    def post(self, request, trip_id, place_id):
        trip = get_object_or_404(Trip, id=trip_id)
        place = get_object_or_404(Place, id=place_id)

        if trip.places.filter(id=place.id).exists():
            trip.places.remove(place)
            messages.add_message(
                request, messages.SUCCESS, 'Removed From Your Trip'
            )
        else:
            trip.places.add(place)
            messages.add_message(
                request, messages.SUCCESS, 'Added To Your Trip'
            )

        return HttpResponseRedirect(
            reverse('place_detail', args=[trip.slug, trip_id, place_id]))


class PlaceRemove(LoginRequiredMixin, View):

    def post(self, request, trip_id, place_id):

        trip = get_object_or_404(Trip, id=trip_id)
        place = get_object_or_404(Place, id=place_id)

        trip.places.remove(place)

        return HttpResponseRedirect(
            reverse('trip_detail', args=[trip.slug, trip_id]))
