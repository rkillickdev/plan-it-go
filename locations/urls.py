from django.urls import path
from .views import DestinationList

urlpatterns = [
    path(
        '',
        DestinationList.as_view(),
        name='destinations'

    )
]
