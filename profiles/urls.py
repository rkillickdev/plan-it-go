from django.urls import path
from .views import ThankYouView, ProfileCreateView


urlpatterns = [
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('create_profile/', ProfileCreateView.as_view(), name='create_profile'),
]