from django.urls import path
from .views import home_view, error_404, error_403, error_500

urlpatterns = [
    path("", home_view, name="home"),
    path("404_test", error_404, name="error_404"),
    path("403_test", error_403, name="error_403"),
    path("500_test", error_500, name="error_500"),
]
