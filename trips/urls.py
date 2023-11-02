from django.urls import path
from .views import (
    TripCreateView,
    TripUpdateView,
    trip_delete,
    TripListView,
    TripDetailView,
    review_create,
    PlaceDetail,
    review_edit,
    review_delete,
    ImageUploadView,
    image_delete,
    PlaceToggle,
    PlaceRemove,
)

urlpatterns = [
    path("create_trip", TripCreateView.as_view(), name="create_trip"),
    path(
        "update_trip/<slug:slug>/<int:pk>",
        TripUpdateView.as_view(),
        name="update_trip",
    ),
    path(
        "<slug:slug>/delete_trip/<int:trip_id>",
        trip_delete,
        name="delete_trip",
    ),
    path("trip_list", TripListView.as_view(), name="trip_list"),
    path(
        "<slug:slug>/<int:trip_id>",
        TripDetailView.as_view(),
        name="trip_detail",
    ),
    path(
        "<slug:slug>/<int:trip_id>/place/<int:place_id>/",
        PlaceDetail.as_view(),
        name="place_detail",
    ),
    path(
        "<slug:slug>/<int:trip_id>/review/<int:place_id>/",
        review_create,
        name="review",
    ),
    path(
        "<slug:slug>/<int:trip_id>/review/<int:place_id>/edit_review/<int:review_id>",
        review_edit,
        name="edit_review",
    ),
    path(
        "<slug:slug>/<int:trip_id>/review/<int:place_id>/delete_review/<int:review_id>",
        review_delete,
        name="delete_review",
    ),
    path(
        "<slug:slug>/<int:trip_id>/images/<int:place_id>/",
        ImageUploadView.as_view(),
        name="add_image",
    ),
    path(
        "<slug:slug>/<int:trip_id>/images/<int:place_id>/delete_image/<int:image_id>",
        image_delete,
        name="delete_image",
    ),
    path(
        "toggle_place/<int:trip_id>/<int:place_id>",
        PlaceToggle.as_view(),
        name="toggle_place",
    ),
    path(
        "remove_place/<int:trip_id>/<int:place_id>",
        PlaceRemove.as_view(),
        name="remove_place",
    ),
]
