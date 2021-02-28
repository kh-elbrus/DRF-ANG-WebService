from .models import Article
from rest_framework import generics, viewsets, mixins 
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from core.models import Tag, Technology, Post
from . import serializers


class BasePostAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                          mixins.CreateModelMixin):
    """Base viewset for user owned post attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')


    def perform_create(self, serializer):
        """Create a new tech"""
        serializer.save(user=self.request.user)

class TagViewSet(BasePostAttrViewSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

class TechnologyViewSet(BasePostAttrViewSet):
    """Manage technologies in the database"""
    queryset = Technology.objects.all()
    serializer_class = serializers.TechnologySerializer


class PostViewSet(viewsets.ModelViewSet):
    """Manage posts in the database"""
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
    authentication_classes = {TokenAuthentication, }
    permission_classes = {IsAuthenticated, }

    def get_queryset(self):
        """Retrieving the posts for the auth user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.PostDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new post"""
        serializer.save(user=self.request.user)