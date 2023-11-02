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


class PlaceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "place-api-form"
        self.fields["location"].label = "Select A Destination"
        self.helper.form_method = "POST"

        self.helper.layout = Layout(
            Field("location", css_class="mt-2"),
            Div(
                Submit("Submit", "Request Places", css_id="submitButton"),
                css_class="my-4",
            ),
        )

    class Meta:
        model = Place
        fields = ["location"]


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "reviewForm"
        self.helper.form_show_labels = False
        self.helper.form_method = "POST"

        self.helper.layout = Layout(
            Field("body", placeholder="Tell us more about your visit..."),
            Div(
                Submit(
                    "Submit",
                    "Post Review",
                    css_id="submitButton",
                    css_class="btn btn-dark",
                ),
                css_class="my-4 text-center",
            ),
        )

    class Meta:
        model = Review
        fields = ["body"]


class ImageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "imageForm"
        self.fields["path"].label = False
        self.helper.form_method = "POST"

        self.helper.layout = Layout(
            Field("path"),
            Div(
                Submit(
                    "Submit",
                    "Upload",
                    css_id="imageUploadButton",
                    css_class="btn btn-dark",
                ),
                css_class="my-4 text-center",
            ),
        )

    class Meta:
        model = Image
        fields = ["path"]
