from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag

from mlarticles.serializers import TagSerializer


TAGS_URL = reverse("mlarticles:tag-list")


class PublicTagsApiTests(TestCase):
    """Test the publicly avaliable tags API"""

    def setUp(self):
        self.client = APIClient()


    def test_login_required(self):
        """Test that login is required for retrieving tags"""
        resp = self.client.get(TAGS_URL)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTests(TestCase):
    """Test the authorized user tags APi"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@iuca.kg',
            'test-iuca-pwd'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """Test retrieving tags"""
        Tag.objects.create(user=self.user, name='Self-Development')
        Tag.objects.create(user=self.user, name='Leadership')
        Tag.objects.create(user=self.user, name='Startups')

        resp = self.client.get(TAGS_URL)

        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, serializer.data)

    def test_tags_limited_to_user(self):
        """Test that tags returned are for the auth user"""
        un_user = get_user_model().objects.create_user(
            'unuser@iuca.kg',
            'test-iuca-pwd'
        )
        Tag.objects.create(user=un_user, name="UnTest")
        tag = Tag.objects.create(user=self.user, name="Foods")

        resp = self.client.get(TAGS_URL)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]['name'], tag.name)

    def test_create_tag_successful(self):
        """Test creating a new tag"""
        payload = {'name': 'First Tag'}
        self.client.post(TAGS_URL, payload)

        exists = Tag.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()

        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """Test creating a new tag with invalid payload"""
        payload = {'name': ''}
        resp = self.client.post(TAGS_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        