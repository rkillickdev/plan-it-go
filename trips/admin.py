from django.contrib import admin
from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    """
    Defines list display and search fields.
    """

    list_display = ("title", "location", "profile")
    search_fields = ["title", "location__city", "profile__screen_name"]
