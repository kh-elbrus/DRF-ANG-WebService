from .models import Article
from core.models import Tag, Technology, Post
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""
    
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id', )


class TechnologySerializer(serializers.ModelSerializer):
    """Serializer for technology objects"""
    
    class Meta:
        model = Technology
        fields = ('id', 'name', )
        read_only_fields = ('id', )


class PostSerializer(serializers.ModelSerializer):
    """Serialize a post"""

    technologies = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Technology.objects.all()
    )
    
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )
    
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'preview', 'description', 'body', 'link', 'technologies', 'tags',
        )
        read_only_fields = ('id', )


class PostDetailSerializer(PostSerializer):
    """Serialize a post detail"""
    technologies = TechnologySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)


class PostImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to post"""

    class Meta:
        model = Post
        fields = ('id', 'preview')
        read_only_fields = ('id', )