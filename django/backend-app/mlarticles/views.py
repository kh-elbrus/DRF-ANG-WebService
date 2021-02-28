from rest_framework.decorators import action
from rest_framework.response import Response 

from .models import Article
from rest_framework import generics, viewsets, mixins, status
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
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(post__isnull=False)
        return queryset.filter(user=self.request.user).order_by('-name').distinct()


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

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieving the posts for the auth user"""
        tags = self.request.query_params.get('tags')
        technologies = self.request.query_params.get('technologies')
        queryset = self.queryset
        
        if tags:
            tag_ids = self._params_to_ints(tags)
            queryset = queryset.filter(tags__id__in=tag_ids)

        if technologies:
            tech_ids = self._params_to_ints(technologies)
            queryset = queryset.filter(technologies__id__in=tech_ids)

        return queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.PostDetailSerializer
        elif self.action == 'upload_image':
            return serializers.PostImageSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new post"""
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload image to a post"""
        post = self.get_object()
        serializer = self.get_serializer(
            post,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
