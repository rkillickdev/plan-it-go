from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """
    Defines method for admin to approve locations
    in the Django admin panel
    """
    list_display = ('city', 'approved')
    
    def approve_locations(self, request, queryset):
        queryset.update(approved=True)
