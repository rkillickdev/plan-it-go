from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    """
    Prepopulates slug field with screen name
    """

    prepopulated_fields = {"slug": ("screen_name",)}
    summernote_fields = "about"
