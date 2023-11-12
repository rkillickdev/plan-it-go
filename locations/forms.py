from django import forms
from django.urls import reverse
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Submit,
    Layout,
    Hidden,
    Fieldset,
    Field,
    Div,
    HTML,
)
from .models import Location


class LocationForm(ModelForm):
    latitude = forms.DecimalField(widget=forms.TextInput())
    longitude = forms.DecimalField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "location-form"
        self.helper.form_class ="rounded bg-dark text-light p-4"
        self.helper.form_show_labels = False
        self.helper.form_method = "POST"

        self.helper.layout = Layout(
            Field(
                "city", css_class="mb-4", placeholder="Enter a City Location"
            ),
            Field(
                "summary",
                css_class="mb-4",
                placeholder="Destination synopsis...",
            ),
            Field(
                "latitude",
                css_class="mb-4",
                placeholder="Destination latitude",
            ),
            Field(
                "longitude",
                css_class="mb-4",
                placeholder="Destination longitude",
            ),
            Field("image", css_class="mb-4"),
            Div(
                Submit(
                    "Submit",
                    "Create",
                    css_id="submit-button",
                    css_class="btn btn-primary text-light",
                ),
                css_class="mt-4 text-center",
            ),
        )

    class Meta:
        model = Location

        fields = ["city", "summary", "latitude", "longitude", "image"]
