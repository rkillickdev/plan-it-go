from django import forms
from .models import Trip
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden, Fieldset, Field, Div, HTML


class TripForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'trip-form'
        # self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.fields['location'].label = 'Where are you going?'
        self.fields['title'].label = False
        self.fields['description'].label = False
        self.fields['trip_image'].label = 'Add your own image'
        self.fields['start_date'].label = 'When do you go?'
        self.fields['end_date'].label = 'When do you come back?'

        self.helper.layout = Layout(
            Div(
                HTML("""
                <h2>Create your trip...</h2>
                """), css_class="py-2 text-center"),
            Field('location', css_class="mb-4"),
            Field('title', css_class="mb-4", placeholder='Give your trip a name'),
            Field('description', css_class="mb-4", placeholder='Tell us about your trip...'),
            Field('trip_image', css_class="mb-4"),
            Field('start_date', css_class="mb-4"),
            Field('end_date', css_class="mb-4"),
            Div(
                Submit('Submit', 'Create Trip', css_id='submitButton'),
                css_class="mb-4"
            )
        )

    class Meta:
        model = Trip
        fields = [
            'location', 'title', 'description', 'trip_image', 'start_date',
            'end_date'
        ]
