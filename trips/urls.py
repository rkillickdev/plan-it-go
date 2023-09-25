from django.urls import path
from .views import (
    TripCreateView,
    TripUpdateView,
    TripListView,
    TripDetailView,
    TripRecommendationsView,
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
        '<slug:slug>/<int:pk>',
        TripDetailView.as_view(),
        name='trip_detail'
    ),
    path(
        'recommendations/<slug:slug>/<int:pk>',
        TripRecommendationsView.as_view(),
        name='trip_recommendations'
    ),
    path(
        'add_place/<int:trip_id>/<int:place_id>',
        PlaceAdd.as_view(),
        name='add_place'
    )
]
