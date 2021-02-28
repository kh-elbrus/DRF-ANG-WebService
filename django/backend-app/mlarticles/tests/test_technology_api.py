from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Technology

from mlarticles.serializers import TechnologySerializer


TECHNOLOGY_URL = reverse('mlarticles:technology-list')


class PublicTechnologyApiTests(TestCase):
    """Test the publically available technology API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required to access this endpoint"""
        resp = self.client.get(TECHNOLOGY_URL)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTechnologyAPITests(TestCase):
    """Test technology can be retrieved by authorized user"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@iuca.kg',
            'test-iuca-pwd'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_technology_list(self):
        """Test retrieving a list of technology"""
        Technology.objects.create(user=self.user, name='Python')
        Technology.objects.create(user=self.user, name='Angular')

        resp = self.client.get(TECHNOLOGY_URL)

        technologies = Technology.objects.all().order_by('-name')
        serializer = TechnologySerializer(technologies, many=True)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, serializer.data)

    def test_technologies_limited_to_user(self):
        """Test that only technologies for authenticated user are returned"""
        user2 = get_user_model().objects.create_user(
            'other@iuca.kg',
            'other-iuca-pwd'
        )
        Technology.objects.create(user=user2, name='JS')

        technologies = Technology.objects.create(user=self.user, name='Java')

        resp = self.client.get(TECHNOLOGY_URL)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]['name'], technologies.name)

    def test_create_tech_successful(self):
        """Test create a new technology"""
        payload = {'name': 'Ffuf'}
        self.client.post(TECHNOLOGY_URL, payload)

        exists = Technology.objects.filter(
            user=self.user,
            name=payload['name'],
        ).exists()

        self.assertTrue(exists)

    def test_create_trch_invalid(self):
        """Test creating a new tech with invalid payload"""
        payload = {'name': ''}
        resp = self.client.post(TECHNOLOGY_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)