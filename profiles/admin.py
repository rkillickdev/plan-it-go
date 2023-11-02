from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("screen_name",)}
    summernote_fields = "about"
