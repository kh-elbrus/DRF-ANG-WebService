from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email="test@iuca.kg", password="test-iuca-pwd"):
    """Create a simple user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@iuca.kg"
        password = "iuca-test-pwd"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@IUCA.KG"
        user = get_user_model().objects.create_user(email, "iuca-test-pwd")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "iuca-test-pwd")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@iuca.kg", "iuca-test-pwd"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the Tag string represintation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Self-Development"
        )

        self.assertEqual(str(tag), tag.name)
