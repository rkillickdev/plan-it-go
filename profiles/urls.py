from django.urls import path
from .views import (ProfileRegisterView,
                    ProfileDetailView,
                    ProfileUpdateView
                    )


urlpatterns = [
    path(
        'profile_register',
        ProfileRegisterView.as_view(),
        name='profile_register'
    ),
    path(
        'profile_detail/<int:pk>',
        ProfileDetailView.as_view(),
        name='profile_detail'
    ),
    path(
        'update_profile/<int:pk>',
        ProfileUpdateView.as_view(),
        name='update_profile'
    ),
]
