from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    url = serializers.URLField()

    def create(self, validated_data):
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.password = make_password(validated_data.get('password'))
        instance.profile.url = validated_data.get('url')
        instance.save()
        return instance

    def validate_username(self, username):
        if (self.instance is None or self.instance.username != username) and User.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario {0} no está disponible".format(username))
        return username

    def validate_email(self, email):
        if (self.instance is None or self.instance.email != email) and User.objects.filter(email=email).exists():
            raise ValidationError("El email {0} ya está en uso".format(email))
        return email.lower()