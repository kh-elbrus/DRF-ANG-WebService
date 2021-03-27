from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path("api/v1/token/refresh/", TokenRefreshView.as_view()),
    path("api/v1/token/verify/", TokenVerifyView.as_view()),
    path("api/v1/user/", include("user.urls")),
    path("api/v1/article/", include("mlarticles.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
