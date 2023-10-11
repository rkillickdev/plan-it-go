from django import forms
from .models import Profile
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden, Fieldset, Field, Div, HTML
from crispy_forms.layout import Submit


class ProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'profile-form'
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Div(
                HTML("""
                <h2>Make A Profile</h2>
                """), css_class="py-2"),
            Field('first_name', placeholder='First Name'),
            Field('surname', placeholder='Surname'),
            Field('screen_name', placeholder='Give yourself a screen name...'),
            Field('date_of_birth', placeholder='When were you born?'),
            Field('about', placeholder='Tell us about you...'),
            Field('profile_image'),
            Div(
                Submit('Submit', 'Create Profile', css_id='submitButton'),
                css_class="my-4"
            )
            )

    class Meta:
        model = Profile
        fields = ['first_name', 'surname', 'screen_name', 'date_of_birth',
                  'about', 'profile_image']
