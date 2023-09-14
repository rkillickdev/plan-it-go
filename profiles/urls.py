from django.urls import path
from .views import (ProfileRegisterView, ProfileUpdateView)


urlpatterns = [
    path(
        'profile_register',
        ProfileRegisterView.as_view(),
        name='profile_register'
    ),
    path(
        'update_profile/<int:pk>',
        ProfileUpdateView.as_view(),
        name='update_profile'
    ),
]
