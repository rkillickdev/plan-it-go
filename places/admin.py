from django.contrib import admin
from .models import Place
from .models import Review

admin.site.register(Place)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
