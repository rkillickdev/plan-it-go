from django import forms
from .models import Profile
from django.forms import ModelForm
from allauth.account.forms import LoginForm, SignupForm
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


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "profile-form"
        self.helper.form_show_labels = False
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            Field("first_name", css_class="mb-4", placeholder="First Name"),
            Field("surname", css_class="mb-4", placeholder="Surname"),
            Field(
                "screen_name",
                css_class="mb-4",
                placeholder="Give yourself a screen name...",
            ),
            Field(
                "about", css_class="mb-4", placeholder="Tell us about you..."
            ),
            Field("profile_image", css_class="mb-4"),
            Div(
                Submit(
                    "Submit",
                    "Create Profile",
                    css_id="submitButton",
                    css_class="btn btn-dark",
                ),
                css_class="mb-4 text-center",
            ),
        )

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "surname",
            "screen_name",
            "about",
            "profile_image",
        ]


class CustomLoginForm(LoginForm):
    """
    Used this following example to help with styling of Django allauth forms:
    https://gist.github.com/ambivalentno/9d6828fe8b5d894a6f2d
    """

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.field_class = "mb-4"
        self.fields["login"].label = False
        self.fields["password"].label = False

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
                Submit(
                    "Submit",
                    "Log In",
                    css_id="signin-button",
                    css_class="btn btn-dark",
                ),
                css_class="mt-4",
            )
        )


class CustomSignupForm(SignupForm):
    """
    Used this following example to help with styling of Django allauth forms:
    https://gist.github.com/ambivalentno/9d6828fe8b5d894a6f2d
    """

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.field_class = "mb-4"
        self.helper.form_show_labels = False

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
                Submit(
                    "Submit",
                    "Sign Up",
                    css_id="signup-button",
                    css_class="btn btn-dark",
                ),
                css_class="mt-4",
            )
        )

