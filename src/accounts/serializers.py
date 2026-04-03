from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['bio', 'avatar_url', 'followers_count', 'following_count', 'created_at']
        read_only_fields = ['followers_count', 'following_count', 'created_at']

    def get_followers_count(self, obj):
        return obj.user.followers.count()

    def get_following_count(self, obj):
        return obj.user.following.count()


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
