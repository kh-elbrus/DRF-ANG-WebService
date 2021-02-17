from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse("user:create")
TOKEN_URL = reverse("user:token")
ME_URL = reverse("user:me")


def create_user(**param):
    return get_user_model().objects.create_user(**param)


class PublicUserApiTests(TestCase):
    """Test the users api public"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            "email": "test@iuca.kg",
            "password": "test-iuca-pwd",
            "name": "Full name of user",
        }
        resp = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**resp.data)
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", resp.data)

    def test_user_exists(self):
        """Test creating user that already exist"""
        payload = {"email": "test@iuca.kg", "password": "test-iuca-pwd"}
        create_user(**payload)

        resp = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the PWD must be more 8 characters"""
        payload = {"email": "test@iuca.kg", "password": "test"}
        resp = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test that token is created for user"""
        payload = {"email": "test@iuca.kg", "password": "test-iuca-pwd"}
        create_user(**payload)
        resp = self.client.post(TOKEN_URL, payload)

        self.assertIn("token", resp.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_creds(self):
        """Test that token is not created if invalid creds are given"""
        create_user(email="test@iuca.kg", password="test-pwd")
        payload = {"email": "test@iuca.kg", "password": "NotTruePWD"}
        resp = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("token", resp.data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token not created if user does not exist"""
        payload = {"email": "test@iuca.kg", "password": "test-iuca-pwd"}
        resp = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("token", resp.data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        payload = {"email": "test", "password": ""}
        resp = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("token", resp.data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """Test that authontication required for users"""
        resp = self.client.get(ME_URL)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserAPITest(TestCase):
    """Test API requests that require authotication"""

    def setUp(self):
        self.user = create_user(
            email="test@iuca.kg", password="test-iuca-pwd", name="Name test"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        """Test retrieving profile for logged in used"""
        resp = self.client.get(ME_URL)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(
            resp.data,
            {
                "name": self.user.name,
                "email": self.user.email,
            },
        )

    def test_post_me_not_allowed(self):
        """Test that POST is not allowed on the me url"""
        resp = self.client.post(ME_URL, {})

        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """Test updating the user profile for authenticate user"""
        payload = {"name": "new name", "password": "new-test-iuca-pwd"}
        resp = self.client.patch(ME_URL, payload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.name, payload["name"])
        self.assertTrue(self.user.check_password(payload["password"]))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
