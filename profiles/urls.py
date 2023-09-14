from django.urls import path
from .views import (ThankYouView, ProfileCreateView,
                    ProfileUpdateView
                    )


urlpatterns = [
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('create_profile/', ProfileCreateView.as_view(), name='create_profile'),
    path('update_profile/<int:pk>', ProfileUpdateView.as_view(), name='update_profile'),
]
