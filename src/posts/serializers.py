from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Comment, Like, Post


class PostAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(serializers.ModelSerializer):
    author = PostAuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    author = PostAuthorSerializer(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'updated_at', 'likes_count', 'comments_count', 'is_liked']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def get_is_liked(self, obj):
        # Uses the prefetched 'user_likes' attr set in the view queryset — no extra query per post
        user_likes = getattr(obj, 'user_likes', None)
        if user_likes is not None:
            return len(user_likes) > 0
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False
