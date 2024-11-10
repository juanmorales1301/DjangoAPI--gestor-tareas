from rest_framework import serializers
from ..models.post import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published', 'author', 'create_at', 'publish_at']
        read_only_fields = ['author', 'create_at', 'publish_at']
