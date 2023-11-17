from django.contrib import admin
from .models import Place
from .models import Review
from .models import Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "rating", "approved")
    search_fields = ["location__city", "rating"]

    def approve_places(self, request, queryset):
        queryset.update(approved=False)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("place", "profile", "created_on", "approved")
    search_fields = ["place__name", "profile__screen_name", "approved"]

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("place", "profile", "created_on", "approved")
    search_fields = ["place__name", "profile__screen_name", "approved"]

    def approve_images(self, request, queryset):
        queryset.update(approved=True)
