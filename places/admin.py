from django.contrib import admin
from .models import Place
from .models import Review
from .models import Image

admin.site.register(Place)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    def approve_images(self, request, queryset):
        queryset.update(approved=True)
