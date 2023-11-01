from django.urls import path
from .views import get_places, PlaceListView, PlaceBrowseDetail

urlpatterns = [
    path(
        'get_places/<int:destination_id>/<slug:slug>',
        get_places,
        name='get_places'
    ),
    path(
        '<int:location_id>/<slug:slug>',
        PlaceListView.as_view(),
        name='place_list'
    ),
    path(
        '<slug:slug>/<int:pk>',
        PlaceBrowseDetail.as_view(),
        name='place_browse_detail'
    )

]
