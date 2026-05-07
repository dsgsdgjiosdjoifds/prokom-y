from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['bio', 'avatar_url', 'followers_count', 'following_count', 'created_at']
        read_only_fields = ['followers_count', 'following_count', 'created_at']

    @extend_schema_field(serializers.IntegerField())
    def get_followers_count(self, obj):
        return obj.user.followers.count()

    @extend_schema_field(serializers.IntegerField())
    def get_following_count(self, obj):
        return obj.user.following.count()


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']
