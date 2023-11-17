from django.test import TestCase
from .forms import ProfileForm, CustomLoginForm, CustomSignupForm


class TestLoginForm(TestCase):
    """
    Tests for Custom Login Form
    """

    def test_login_form_invalid_required_fields_blank(self):
        """
        Test if user login form is invalid if any fields are blank
        """

        form = CustomLoginForm({"login": "", "password": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("login", form.errors.keys())
        self.assertIn("password", form.errors.keys())
        self.assertEqual(form.errors["login"][0], "This field is required.")
        self.assertEqual(form.errors["password"][0], "This field is required.")


class TestSignUpForm(TestCase):
    """
    Tests for Custom Signup Form
    """

    def test_sign_up_form_valid(self):
        """
        Tests if sign up form is valid
        """
        form = CustomSignupForm(
            {
                "username": "John",
                "password1": "testpassword1976!",
                "password2": "testpassword1976!",
            }
        )
        self.assertTrue(form.is_valid())

    def test_sign_up_form_invalid_if_required_fields_blank(self):
        """
        Tests if sign up form is invalid if required fields are blank
        """
        form = CustomSignupForm(
            {"username": "", "password1": "", "password2": ""}
        )
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors.keys())
        self.assertIn("password1", form.errors.keys())
        self.assertIn("password2", form.errors.keys())
        self.assertEqual(form.errors["username"][0], "This field is required.")
        self.assertEqual(
            form.errors["password1"][0], "This field is required."
        )
        self.assertEqual(
            form.errors["password2"][0], "This field is required."
        )

    def test_sign_up_form_invalid_if_passwords_non_matching(self):
        """
        Tests if sign up form is invalid if passwords do not match
        """

        form = CustomSignupForm(
            {
                "username": "John",
                "password1": "testpassword1976!",
                "password2": "testpassword1977!",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors.keys())
        self.assertEqual(
            form.errors["password2"][0],
            "You must type the same password each time.",
        )


class TesTProfileForm(TestCase):
    """
    Tests for Profile Form
    """

    def test_profile_form_invalid(self):
        """
        Tests if profile form is valid
        """
        form = ProfileForm(
            {
                "first_name": "John",
                "surname": "Smith",
                "screen_name": "smithy76",
                "about": "I love to travel",
            }
        )
        self.assertTrue(form.is_valid())

    def test_profile_form_invalid_if_max_length_exceeded(self):
        """
        Test if profile form is invalid when fields with max
        length are exceeded.
        """

        form = ProfileForm(
            {
                "first_name": str("x" * 51),
                "surname": str("y" * 51),
                "screen_name": str("z" * 26),
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("first_name", form.errors.keys())
        self.assertIn("surname", form.errors.keys())
        self.assertIn("screen_name", form.errors.keys())
        self.assertEqual(
            form.errors["first_name"][0],
            "Ensure this value has at most 50 characters (it has 51).",
        )
        self.assertEqual(
            form.errors["surname"][0],
            "Ensure this value has at most 50 characters (it has 51).",
        )
        self.assertEqual(
            form.errors["screen_name"][0],
            "Ensure this value has at most 25 characters (it has 26).",
        )

    def test_profile_form_invalid_if_required_fields_blank(self):
        """
        Test if profile form is invalid if required fields are blank
        """

        form = ProfileForm(
            {
                "first_name": "",
                "surname": "",
                "screen_name": "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("first_name", form.errors.keys())
        self.assertIn("surname", form.errors.keys())
        self.assertIn("screen_name", form.errors.keys())
        self.assertEqual(
            form.errors["first_name"][0], "This field is required."
        )
        self.assertEqual(form.errors["surname"][0], "This field is required.")
        self.assertEqual(
            form.errors["screen_name"][0], "This field is required."
        )
