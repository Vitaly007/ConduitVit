from rest_framework import serializers
from rest_framework_hstore.serializers import HStoreSerializer

from socnet.apps.authentication.serializers import UserSerializer
from .models import Post, PostLike


class PostSerializer(HStoreSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'owner',
            'post',
        )

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post


class PostLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PostLike
        fields = ('id', 'user', 'like')
