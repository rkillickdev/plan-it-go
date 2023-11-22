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
    """
    Form for Location Model.  Crispy forms helper used for
    layout and styling.
    """

    latitude = forms.DecimalField(widget=forms.TextInput())
    longitude = forms.DecimalField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "location-form"
        self.helper.form_class = "rounded bg-dark text-light p-4"
        self.fields["city"].label = False
        self.fields["summary"].label = False
        self.fields["latitude"].label = False
        self.fields["longitude"].label = False
        self.fields["image"].label = False
        self.helper.form_method = "POST"

        self.helper.layout = Layout(
            Field(
                "city",
                css_class="mb-4",
                aria_label="Enter a city location",
                placeholder="Enter a City Location",
            ),
            Field(
                "summary",
                css_class="mb-4",
                aria_label="Enter a synopsis for the selected locatio",
                placeholder="Destination synopsis...",
            ),
            Field(
                "latitude",
                css_class="",
                aria_label="Enter a latitude for the selected location",
                placeholder="Destination latitude",
            ),
            Field(
                "longitude",
                css_class="mt-4",
                aria_label="Enter a longitude for the selected location",
                placeholder="Destination longitude",
            ),
            Div(
                HTML("<p>Add an image</p>"),
                css_class="mt-4"
            ),
            Field("image", css_class="form-select file-upload-input px-2 py-3"),
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
