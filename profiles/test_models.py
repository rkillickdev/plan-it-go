from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class TestProfileModel(TestCase):
    """
    Tests Profile Model
    """

    def setUp(self):
        """
        Create an instance of the class Profile and set attributes
        """

        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpassword"
        )
        self.profile = Profile.objects.get(user=self.user)
        self.profile.first_name = "Rob"
        self.profile.surname = "Killick"
        self.profile.screen_name = "rkillickdev"
        self.profile.slug = "rkillickdev"
        self.profile.date_of_birth = 2022-9-15
        self.profile.about = "Test Bio"
        self.profile.profile_image = "test.jpg"
        self.expected_str = self.user.username

    def test_profile_model(self):
        """
        Tests the attibutes in the Profile model
        """

        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.first_name, "Rob")
        self.assertEqual(self.profile.surname, "Killick")
        self.assertEqual(self.profile.screen_name, "rkillickdev")
        self.assertEqual(self.profile.slug, "rkillickdev")
        self.assertEqual(self.profile.date_of_birth, 2022-9-15)
        self.assertEqual(self.profile.about, "Test Bio")
        self.assertEqual(self.profile.profile_image, "test.jpg")
        self.assertEqual(str(self.profile), self.expected_str)
