from .models import Article
from core.models import Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id', )


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for the articles object"""

    class Meta:
        model = Article
        fields = '__all__'
        