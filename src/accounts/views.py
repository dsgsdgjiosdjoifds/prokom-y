from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Follow
from .serializers import ProfileSerializer, UserSerializer


class OwnProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def patch(self, request):
        serializer = ProfileSerializer(request.user.profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(UserSerializer(request.user).data)


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = User.objects.select_related('profile')


class FollowersListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        target = get_object_or_404(User, username=self.kwargs['username'])
        return User.objects.filter(following__following=target).select_related('profile')


class FollowingListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        target = get_object_or_404(User, username=self.kwargs['username'])
        return User.objects.filter(followers__follower=target).select_related('profile')


class FollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        target = get_object_or_404(User, username=username)
        if target == request.user:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        Follow.objects.get_or_create(follower=request.user, following=target)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, username):
        target = get_object_or_404(User, username=username)
        Follow.objects.filter(follower=request.user, following=target).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
