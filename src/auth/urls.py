from django.urls import path
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView


@extend_schema(
    tags=['Auth'],
    summary='Login',
    description='Obtain a JWT access and refresh token pair using username and password.',
)
class LoginView(TokenObtainPairView):
    pass


@extend_schema(
    tags=['Auth'],
    summary='Refresh token',
    description='Exchange a valid refresh token for a new access token.',
)
class RefreshView(TokenRefreshView):
    pass


urlpatterns = [
    path('/login', LoginView.as_view(), name='token_obtain'),
    path('/register', RegisterView.as_view(), name='register'),
    path('/refresh', RefreshView.as_view(), name='token_refresh'),
]
