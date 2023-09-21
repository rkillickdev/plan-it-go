from django.urls import path
from .views import get_places, PlaceListView

urlpatterns = [
    path(
        'get_places',
        get_places,
        name='get_places'
    ),
    path(
        '<slug:slug>',
        PlaceListView.as_view(),
        name='place_list'
    )
]
