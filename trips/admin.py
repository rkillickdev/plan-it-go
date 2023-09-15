from django.contrib import admin
from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
