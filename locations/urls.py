from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from .views import CreateDestination, UpdateDestination

urlpatterns = [
    path(
        "",
        staff_member_required(CreateDestination.as_view()),
        name="locations",
    ),
    path(
        "update_destination/<int:location_id>/<slug:slug>",
        staff_member_required(UpdateDestination.as_view()),
        name="update_destination",
    ),
]
