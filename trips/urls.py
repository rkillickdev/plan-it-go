from django.urls import path
from .views import (
    TripCreateView,
    TripUpdateView,
    TripListView,
    TripDetailView,
    TripRecommendationsView,
    place_detail,
    PlaceAdd,
)

urlpatterns = [
    path(
        'create_trip',
        TripCreateView.as_view(),
        name='create_trip'
    ),
    path(
        'update_trip/<slug:slug>/<int:pk>',
        TripUpdateView.as_view(),
        name='update_trip'
    ),
    path(
        'trip_list',
        TripListView.as_view(),
        name='trip_list'
    ),
    path(
        '<slug:slug>/<int:trip_id>',
        TripDetailView.as_view(),
        name='trip_detail'
    ),
    path(
        'recommendations/<slug:slug>/<int:trip_id>',
        TripRecommendationsView.as_view(),
        name='trip_recommendations'
    ),
    path(
        'recommendations/<slug:slug>/<int:trip_id>/place/<int:place_id>',
        place_detail,
        name='place_detail'
    ),
    path(
        'add_place/<int:trip_id>/<int:place_id>',
        PlaceAdd.as_view(),
        name='add_place'
    )
]
