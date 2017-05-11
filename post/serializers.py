from django.contrib.auth.models import User
from rest_framework import serializers

from category.models import Category
from post.models import Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')
        read_only_fields = ('id', 'username'),


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("cat_id", "name")
        read_only_fields = ('cat_id', 'name'),


class PostListSerializar(serializers.ModelSerializer):
    author = UserSerializer()
    categories = CategorySerializer(many=True, read_only=True)
    num_com = serializers.CharField(source='num_post_comentary')

    class Meta:
        model = Post
        fields = ("post_id", "title", "intro", "url_media", "categories", "publicate_at", "author", "likes", "num_com")
        read_only_fields = ('author', 'num_com', 'url_media'),
