import tempfile
import os

from PIL import Image

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Post, Tag, Technology

from mlarticles.serializers import PostSerializer, PostDetailSerializer


POST_URL = reverse('mlarticles:post-list')


def image_upload_url(post_id):
    """Return URL for post image upload"""
    return reverse('mlarticles:post-upload-image', args=[post_id])


def detail_url(post_id):
    """Return post detail URL"""
    return reverse('mlarticles:post-detail', args=[post_id])


def sample_post(user, **params):
    """Create and return a sample post"""
    defaults = {
        'title': 'Sample test',
        'description': 'Test',
        'body': 'Test',
    }
    defaults.update(params)

    return Post.objects.create(user=user, **defaults)


def sample_tag(user, name='test tag'):
    """Create and return a sample tag"""
    return Tag.objects.create(user=user, name=name)


def sample_tech(user, name='test tech'):
    """Create and return a sample tech"""
    return Technology.objects.create(user=user, name=name)


class PublicPostAPITests(TestCase):
    """Test unauth post access"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_is_required(self):
        """test that auth is required"""
        resp = self.client.get(POST_URL)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatePostAPITests(TestCase):
    """Test the authorized user posts APi"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@iuca.kg',
            'test-iuca-pwd',
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_recipes(self):
        """Test retrieving list of posts"""
        sample_post(user=self.user)
        sample_post(user=self.user)

        resp = self.client.get(POST_URL)

        posts = Post.objects.all().order_by('-id')
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, serializer.data)

    def test_posts_limited_for_user(self):
        """Test retrieving posts for user"""
        user2 = get_user_model().objects.create_user(
            'other@iuca.kg',
            'other-iuca-pwd',
        )
        sample_post(user=user2)
        sample_post(user=self.user)

        resp = self.client.get(POST_URL)

        posts = Post.objects.filter(user=self.user)
        serializer = PostSerializer(posts, many=True)
        
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data, serializer.data)

    def test_post_detail_view(self):
        """Test viewing a post detail"""
        post = sample_post(user=self.user)
        post.tags.add(sample_tag(user=self.user))
        post.technologies.add(sample_tech(user=self.user))

        url = detail_url(post.id)
        resp = self.client.get(url)

        serializer = PostDetailSerializer(post)

        self.assertEqual(resp.data, serializer.data)

    def test_create_basic_post(self):
        """Test creating basic post"""
        payloads = {
            'title': 'Cybersecurity | Red teaming',
            'description': 'Web penetration testing',
            'body': 'Using tools ....',
        }
        resp = self.client.post(POST_URL, payloads)

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        post = Post.objects.get(id=resp.data['id'])
        for key in payloads.keys():
            self.assertEqual(payloads[key], getattr(post, key))

    def test_create_post_with_tags(self):
        """Test creating a post with tags"""
        tag1 = sample_tag(user=self.user, name='pentest')
        tag2 = sample_tag(user=self.user, name='cybersec')
        payload = {
            'title': 'Cybersec in ...',
            'description': 'describe this post',
            'body': 'Using tools',
            'tags': [tag1.id, tag2.id],
        }
        resp = self.client.post(POST_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        post = Post.objects.get(id=resp.data['id'])
        tags = post.tags.all()

        self.assertEqual(tags.count(), 2)
        self.assertIn(tag1, tags)
        self.assertIn(tag2, tags)

    def test_create_post_with_tech(self):
        """Test creating a post with technologies"""
        tech1 = sample_tech(user=self.user, name='DRF')
        tech2 = sample_tech(user=self.user, name="Django")
        payload = {
            'title': 'Test this post!',
            'description': 'Test description!',
            'body': 'Text...',
            'technologies': [tech1.id, tech2.id],
        }
        resp = self.client.post(POST_URL, payload)
        
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        post = Post.objects.get(id=resp.data['id'])
        techs = post.technologies.all()

        self.assertEqual(techs.count(), 2)
        self.assertIn(tech1, techs)
        self.assertIn(tech2, techs)

    def test_partial_update_post(self):
        """Test updating a post with patch"""
        post = sample_post(user=self.user)
        post.tags.add(sample_tag(user=self.user))
        new_tag = sample_tag(user=self.user, name='OSINT')
        payload = {
            'title': 'Changed title!',
            'tags': [new_tag.id]
        }

        url = detail_url(post.id)
        self.client.patch(url, payload)

        post.refresh_from_db()

        self.assertEquals(post.title, payload['title'])
        tags = post.tags.all()
        self.assertEquals(len(tags), 1)
        self.assertIn(new_tag, tags)

    def test_full_update_post(self):
        """Test updating a post with PUT"""
        post = sample_post(user=self.user)
        post.tags.add(sample_tag(user=self.user))
        payload = {
            'title': 'Again Changed title!',
            'description': 'Againg but with PUT...',
            'body': 'Hey!',
        }
        url = detail_url(post.id)
        self.client.put(url, payload)

        post.refresh_from_db()

        self.assertEquals(post.title, payload['title'])
        self.assertEquals(post.description, payload['description'])
        self.assertEquals(post.body, payload['body'])
        tags = post.tags.all()
        self.assertEquals(len(tags), 0)


class PostUploadImageTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@iuca.kg',
            'test-iuca-pwd'
        )
        self.client.force_authenticate(self.user)
        self.post = sample_post(user=self.user)

    def tearDown(self):
        self.post.preview.delete()

    def test_upload_image_to_post(self):
        """Test upload image to post"""
        url = image_upload_url(self.post.id)
        with tempfile.NamedTemporaryFile(suffix='.jpg') as ntf:
            img = Image.new('RGB', (10, 10))
            img.save(ntf, format="JPEG")
            ntf.seek(0)
            resp = self.client.post(url, {'preview': ntf}, format='multipart')

        self.post.refresh_from_db()
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
        self.assertIn('preview', resp.data)
        self.assertTrue(os.path.exists(self.post.preview.path))


    def test_upload_image_bad_request(self):
        """Test uploading an invalid image """
        url = image_upload_url(self.post.id)
        resp = self.client.post(url, {'preview': 'notimage!'}, format='multipart')

        self.assertEquals(resp.status_code, status.HTTP_400_BAD_REQUEST)