from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import UserProfile, ReadingProgress
from .serializers import (
    UserProfileSerializer,
    ReadingProgressSerializer,
)
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


class ReadingProgressViewSet(viewsets.ModelViewSet):
    queryset = ReadingProgress.objects.all()
    serializer_class = ReadingProgressSerializer
    permission_classes = [IsAuthenticated]
