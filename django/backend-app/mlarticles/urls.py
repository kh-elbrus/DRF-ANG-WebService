from django.urls import path
from .views import ArticleList

app_name = "mlarticles"

urlpatterns = [
    path('', ArticleList.as_view()),
]