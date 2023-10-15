from django.urls import path
from .views import DestinationList 
from trips.views import TripBrowse

urlpatterns = [
    path(
        '',
        DestinationList.as_view(),
        name='locations'
    ),
    path(
        'trip_inspiration/<int:location_id>/<slug:slug>',
        TripBrowse.as_view(),
        name='trip_browse'
    ),
]
