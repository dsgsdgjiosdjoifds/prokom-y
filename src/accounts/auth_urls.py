from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('/login', TokenObtainPairView.as_view(), name='token_obtain'),
    path('/register', views.RegisterView.as_view(), name='register'),
    path('/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
