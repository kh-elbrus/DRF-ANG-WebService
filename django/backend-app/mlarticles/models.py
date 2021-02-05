import os
import uuid

from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


def article_image_file_path(instance, filename):
    """Generate file path for new article image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/articles/', filename)


class Article(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    preview = models.ImageField(upload_to=article_image_file_path, blank=True, null=True)
    description = RichTextField(max_length=180, blank=False, null=False)
    slug = models.CharField(max_length=240, null=True, blank=False)
    body = RichTextField()
    link = models.CharField(max_length=255, blank=True)
#    tags = models.ManyToManyField('Tag')

    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def __str__(self):
        return self.title
