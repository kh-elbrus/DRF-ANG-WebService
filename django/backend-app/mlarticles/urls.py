from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('technologies', views.TechnologyViewSet)
router.register('posts', views.PostViewSet)

app_name = "mlarticles"


urlpatterns = [
    path('', include(router.urls)),

]