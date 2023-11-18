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
from .models import Place
from .models import Review
from .models import Image
from locations.models import Location


class PlaceForm(ModelForm):
    """
    Form for Place Model.  Crispy forms helper used for
    layout and styling.
    I referenced the following article to ensure that the 
    only location options available in the 'locations' field
    of the form are those without any places associated with
    them:
    https://stackoverflow.com/questions/61712605/reverse-foreign-key-in-filter-of-queryset-in-django
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["location"].queryset = Location.objects.filter(
            places__isnull=True
        ).distinct()
        self.helper = FormHelper()
        self.helper.form_id = "retrieve-places"
        self.helper.form_class = "rounded bg-dark text-light p-4 text-center"
        self.fields["location"].label = "Select A Destination"
        self.helper.form_method = "POST"

        self.helper.layout = Layout(
            Field("location", css_class="mt-2"),
            Div(
                Submit(
                    "Submit",
                    "Request Places",
                    css_id="submitButton",
                    css_class="btn btn-primary text-light",
                ),
                css_class="mt-4",
            ),
        )

    class Meta:
        model = Place
        fields = ["location"]


class ReviewForm(ModelForm):
    """
    Form for Review Model.  Crispy forms helper used for
    layout and styling.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "reviewForm"
        self.helper.form_class = "rounded bg-dark text-light p-4"
        self.helper.form_show_labels = False
        self.helper.form_method = "POST"

        self.helper.layout = Layout(
            Field(
                "body",
                placeholder="Tell us more about your visit...",
                aria_label="Write a description of your trip",
            ),
            Div(
                Submit(
                    "Submit",
                    "Post Review",
                    css_id="submitButton",
                    css_class="btn btn-primary text-light",
                ),
                css_class="mt-4 text-center",
            ),
        )

    class Meta:
        model = Review
        fields = ["body"]


class ImageForm(ModelForm):
    """
    Form for Image Model.  Crispy forms helper used for
    layout and styling.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "imageForm"
        self.helper.form_class = "rounded bg-dark text-light p-4"
        self.fields["path"].label = False
        self.helper.form_method = "POST"

        self.helper.layout = Layout(
            Field(
                "path",
                css_class="form-select",
                aria_label="Select an image",
                ),
            Div(
                Submit(
                    "Submit",
                    "Upload",
                    css_id="imageUploadButton",
                    css_class="btn btn-primary text-light",
                ),
                css_class="mt-4 text-center",
            ),
        )

    class Meta:
        model = Image
        fields = ["path"]
