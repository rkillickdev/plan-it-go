from django import forms
from django.urls import reverse
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden, Fieldset, Field, Div, HTML
from .models import Location


class LocationForm(ModelForm):
    latitude = forms.DecimalField(widget=forms.TextInput())
    longitude = forms.DecimalField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'reviewForm'
        self.helper.form_show_labels = False
        self.helper.form_method = "POST"

        self.helper.layout = Layout(
            Div(
                HTML("""
                <h2>Create a new Trip Destination</h2>
                """), css_class="py-2"),
            Field('city', placeholder='Enter a City Location'),
            Field('summary', placeholder='Destination synopsis...'),
            Field('latitude', placeholder='Destination latitude'),
            Field('longitude', placeholder='Destination longitude'),
            Field('image', placeholder='Upload an image...'),
            Div(
                Submit('Submit', 'Create Destination', css_id='submitButton'),
                css_class="my-4"
            )
        )

    class Meta:
        model = Location

        fields = ['city', 'summary', 'latitude', 'longitude', 'image']

