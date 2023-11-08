from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, DetailView
from .models import Profile
from .forms import ProfileForm


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View to render the profile update form.
    """

    form_class = ProfileForm
    model = Profile
    success_url = reverse_lazy("trip_list")
    success_message = "Thanks, your profile details have been updated"

    def get_object(self, *args, **kwargs):
        obj = super(ProfileUpdateView, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied()
        return obj
