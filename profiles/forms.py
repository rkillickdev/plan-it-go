from django import forms
from .models import Profile
from django.forms import ModelForm
from allauth.account.forms import LoginForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden, Fieldset, Field, Div, HTML


class CustomLoginForm(LoginForm):
    """
    Used this following example to help with styling of Django allauth forms:
    https://gist.github.com/ambivalentno/9d6828fe8b5d894a6f2d
    """
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'my-2'
        self.fields['login'].label = False
        self.fields['password'].label = False

        self.helper.layout.append(
            HTML(
                "{% if redirect_field_value %}"
                "<input type='hidden' name='{{ redirect_field_name }}'"
                " value='{{ redirect_field_value }}' />"
                "{% endif %}"
            )
        )
        self.helper.layout.append(
            Div(
                Submit('Submit', 'Sign In', css_id='signin-button'),
                css_class="btn btn-primary my-4"
            )
        )


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
