from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, ReadingProgressViewSet

router = DefaultRouter()
router.register(r"profiles", UserProfileViewSet, basename="userprofile")
router.register(r"reading-progress", ReadingProgressViewSet, basename="readingprogress")

app_name = "profile"

urlpatterns = [
    path("", include(router.urls)),
]
