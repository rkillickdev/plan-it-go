from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Profile
from .forms import ProfileForm


class ThankYouView(TemplateView):
    template_name = 'profiles/thank_you.html'


class ProfileCreateView(CreateView):
    form_class = ProfileForm
    model = Profile
    # fields = "__all__"
    success_url = reverse_lazy('profiles:thank_you')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    model = Profile
    success_url = reverse_lazy('home')
    # fields = ['first_name', 'surname', 'screen_name', 'date_of_birth',
    #           'about', 'profile_image']
