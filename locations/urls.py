from django.urls import path
from .views import DestinationList, UpdateDestination
from trips.views import TripBrowse

urlpatterns = [
    path("", DestinationList.as_view(), name="locations"),
    path(
        "update_destination/<int:location_id>/<slug:slug>",
        UpdateDestination.as_view(),
        name="update_destination",
    ),
    path(
        "trip_inspiration/<int:location_id>/<slug:slug>",
        TripBrowse.as_view(),
        name="trip_browse",
    ),
]
