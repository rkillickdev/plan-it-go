from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Place


class PlaceForm(ModelForm):

    class Meta:
        model = Place
        fields = ['location']