from django import forms
from .models import Trip, Location
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


class TripForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.filter(approved=True)
        self.helper = FormHelper()
        self.helper.form_id = "trip-form"
        self.helper.form_class ="rounded bg-dark text-light p-4"
        self.helper.form_method = "post"
        self.fields["location"].label = "Choose a destination"
        self.fields["title"].label = False
        self.fields["description"].label = False
        self.fields["trip_image"].label = "Add your own image"

        self.helper.layout = Layout(
            Field("location", css_class="form-select mt-2 mb-4"),
            Field(
                "title", css_class="mb-4", aria_label="Enter A trip name", placeholder="Give your trip a name"
            ),
            Field(
                "description",
                css_class="mb-4",
                aria_label="Enter a trip description",
                placeholder="Tell us about your trip...",
            ),
            Field(
                "trip_image", css_class="form-select"
            ),
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
        model = Trip
        fields = [
            "location",
            "title",
            "description",
            "trip_image"
        ]
