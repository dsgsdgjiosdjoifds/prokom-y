from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer


@extend_schema(
    tags=['Auth'],
    summary='Register a new user',
    description='Create a new user account. Returns the created user\'s username and email.',
)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
