from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics 
from rest_framework.permissions import AllowAny

# Create your views here.
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]