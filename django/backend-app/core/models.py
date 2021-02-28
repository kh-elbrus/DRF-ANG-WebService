import os
import uuid

from django.db import models
from django.conf import settings 
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from ckeditor.fields import RichTextField


def post_image_file_path(instance, filename):
    """Generate file path for new post image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/articles/', filename)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and save new users"""
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and save a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support using email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"


class Tag(models.Model):
    """Tag to be used for post"""
    name = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Technology(models.Model):
    """Technologies to be used for post"""

    class Meta:
        verbose_name_plural = "Technologies"

    name = models.CharField(max_length=200)
    user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Post object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150, blank=False, null=False)
    preview = models.ImageField(upload_to=post_image_file_path, blank=True, null=True)
    description = RichTextField(max_length=180, blank=False, null=False)
    body = RichTextField()
    link = models.CharField(max_length=255, blank=True)
    technologies = models.ManyToManyField('Technology')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title