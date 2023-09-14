from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView
from .models import Profile
from .forms import ProfileForm


class ProfileRegisterView(TemplateView):
    """
    View to render the profile registration page.
    """

    template_name = 'profiles/profile_register.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to render the profile update form.
    """

    form_class = ProfileForm
    model = Profile
    success_url = reverse_lazy('home')
