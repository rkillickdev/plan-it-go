from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from .views import (
    get_places,
    PlaceListView,
    PlaceBrowseDetail,
    PlaceApproveToggle,
)


urlpatterns = [
    path(
        "get_places/<int:destination_id>/<slug:slug>",
        get_places,
        name="get_places",
    ),
    path(
        "<int:location_id>/<slug:slug>",
        PlaceListView.as_view(),
        name="place_list",
    ),
    path(
        "<slug:slug>/<int:pk>",
        PlaceBrowseDetail.as_view(),
        name="place_browse_detail",
    ),
    path(
        "<slug:slug>/<int:place_id>/toggle_approval",
        staff_member_required(PlaceApproveToggle.as_view()),
        name="place_toggle_approval",
    ),
]
