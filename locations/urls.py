from django.urls import path
from .views import CreateDestination, UpdateDestination

urlpatterns = [
    path("", CreateDestination.as_view(), name="locations"),
    path(
        "update_destination/<int:location_id>/<slug:slug>",
        UpdateDestination.as_view(),
        name="update_destination",
    ),
]
