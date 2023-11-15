from django.test import TestCase
from .forms import ProfileForm


class TesTProfileForm(TestCase):
    def test_profile_form_valid(self):
        """
        Tests if profile form is valid
        """
        form = ProfileForm(
            {
                "first_name": "John",
                "surname": "Smith",
                "screen_name": "smithy76",
                "about": "I love to travel"
            }
        )
        self.assertTrue(form.is_valid())

    def test_profile_form_invalid_max_length_exceeded(self):
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
        self.assertIn('first_name', form.errors.keys())
        self.assertIn('surname', form.errors.keys())
        self.assertIn('screen_name', form.errors.keys())

    def test_profile_form_invalid_required_fields_blank(self):
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
        self.assertIn('first_name', form.errors.keys())
        self.assertIn('surname', form.errors.keys())
        self.assertIn('screen_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')
        self.assertEqual(form.errors['surname'][0], 'This field is required.')
        self.assertEqual(form.errors['screen_name'][0], 'This field is required.')
