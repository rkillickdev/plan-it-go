from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Place


class PlaceForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Request Places'))

    class Meta:
        model = Place
        fields = ['location']
