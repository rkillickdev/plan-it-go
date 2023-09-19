from django.urls import path
from .views import TripCreateView, TripListView

urlpatterns = [
    path(
        'create_trip',
        TripCreateView.as_view(),
        name='create_trip'
    ),
    path(
        'trip_list',
        TripListView.as_view(),
        name='trip_list'
    )
]
