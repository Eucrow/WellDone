from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        write_only_fields = ('password',)

    # Override the create method from ModelSerializer because, when a user is saved, Django Rest Framework use
    # objects.create() instead of objects.create_user():
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

