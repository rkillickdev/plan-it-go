from django.urls import path
from . import views

urlpatterns = [
    path(
        'get_places',
        views.get_places,
        name='get_places'
    ),
]
