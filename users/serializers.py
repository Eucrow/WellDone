from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import UserProfile

from rest_auth.serializers import UserDetailsSerializer


# Override the UserDetailSerializer method from django-rest-auth to allow
# update in the same request the field or the profiles model.
class UserSerializer(UserDetailsSerializer):
    bio = serializers.CharField(source="userprofile.bio", max_length=100, allow_blank=True, required=False)
    avatar_url = serializers.URLField(source="userprofile.avatar_url", allow_blank=True, required=False)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('bio', 'avatar_url',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        bio = profile_data.get('bio')
        avatar_url = profile_data.get('avatar_url')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile

        if profile_data:
            if bio:
                profile.bio = bio
            if avatar_url:
                profile.avatar_url = avatar_url
            profile.save()
        return instance

# DE MANU:
# class UserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField()
#
#     def create(self, validated_data):
#         instance = User()
#         return self.update(instance, validated_data)
#
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name')
#         instance.last_name = validated_data.get('last_name')
#         instance.username = validated_data.get('username')
#         instance.email = validated_data.get('email')
#         instance.password = make_password(validated_data.get('password'))
#         instance.save()
#         return instance
#
#     def validate_username(self, username):
#         if (self.instance is None or self.instance.username != username) and User.objects.filter(
#                 username=username).exists():
#             raise ValidationError("El nombre de usuario {0} no está disponible".format(username))
#         return username
#
#     def validate_email(self, email):
#         if (self.instance is None or self.instance.email != email) and User.objects.filter(email=email).exists():
#             raise ValidationError("El email {0} ya está en uso".format(email))
#         return email.lower()
