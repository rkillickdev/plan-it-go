from django.urls import path
from .views import ProfileUpdateView


urlpatterns = [
    path(
        'update_profile/<int:pk>',
        ProfileUpdateView.as_view(),
        name='update_profile'
    )
]
