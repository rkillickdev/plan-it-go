from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden, Fieldset
from .models import Place
from .models import Review


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


class ReviewForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Post Review'))
        # self.helper.add_input(Hidden('place_id', '{{place.id}}'))

        self.helper.layout = Layout(
            Fieldset(
                'Leave A Review',
                'body',
                'user_rating',
                'recommended'
            ),
            # Hidden('place_id', '{{place.id}}'),
            Submit('Submit', 'Post Review')
        )

    class Meta:
        model = Review
        fields = ['body', 'user_rating', 'recommended']
