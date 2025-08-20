from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source="author", read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "author", "author_id", "title", "content", "created_at", "updated_at", "comments_count"]

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source="author", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "author_id", "content", "created_at", "updated_at"]

    def validate(self, attrs):
        # Ensure post exists (DRF will usually handle this, but explicit is fine)
        if not attrs.get("post"):
            raise serializers.ValidationError("Post is required.")
        return attrs

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
