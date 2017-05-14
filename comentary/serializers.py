from django.contrib.auth.models import User
from rest_framework import serializers
from comentary.models import Comentary


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')
        read_only_fields = ('id', 'username'),


class ComentarySerializar(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comentary
        fields = ("com_id", "author", "comentary", "likes", "disikes", "create_at")
