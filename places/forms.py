from django import forms
from django.urls import reverse
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden, Fieldset, Field
from .models import Place
from .models import Review
from .models import Image


class PlaceForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Request Places'))

    class Meta:
        model = Place
        fields = ['location']


class ReviewForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'reviewForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = "POST"

        self.helper.layout = Layout(
            Fieldset(
                'Leave A Review for {{place.name}}',
                'body',
                'user_rating',
                'recommended'
            ),
            Submit('Submit', 'Post Review', css_id='submitButton')
        )

    class Meta:
        model = Review
        fields = ['body', 'user_rating', 'recommended']


class ImageForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'imageForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            Fieldset(
                'upload an image',
                'path'
            ),
            Submit('Submit', 'Upload Image', css_id='imageUploadButton')
        )

    class Meta:
        model = Image
        fields = ['path']
