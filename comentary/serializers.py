from django.contrib.auth.models import User
from rest_framework import serializers
from comentary.models import Comentary
from post.models import Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("post_id", "title")
        read_only_fields = ("post_id", "title"),


class ComentarySerializar(serializers.ModelSerializer):
    author = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comentary
        fields = ("com_id", "author", "post", "comentary", "likes", "disikes", "create_at")
