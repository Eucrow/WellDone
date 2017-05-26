from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from users.models import Profile


class UserSerializer(ModelSerializer):
    class Meta:
            model = User
            fields = ('id', 'first_name', 'email')


class ProfileSerializer(ModelSerializer):

    user_profile = UserSerializer(source='id', read_only=True)
    bio = serializers.CharField(max_length=100)
    avatar_url = serializers.URLField()

    class Meta(UserSerializer.Meta):
        model = Profile
        fields = ('bio', 'avatar_url', 'user_profile')


# class UserSerializer(UserDetailsSerializer):
#
#     bio = serializers.CharField(max_length=100)
#     avatar_url = serializers.URLField()
#
#     class Meta(UserDetailsSerializer.Meta):
#         fields = UserDetailsSerializer.Meta.fields + ('bio', 'avatar_url',)
#
#     # def update(self, instance, validated_data):
#     #     profile_data = validated_data.pop('userprofile', {})
#     #     bio = profile_data.get('bio')
#     #     avatar_url = profile_data.get('avatar_url')
#     #
#     #     instance = super(UserSerializer, self).update(instance, validated_data)
#     #
#     #     # get and update user profile
#     #     profile = instance.userprofile
#     #     if profile_data and bio and avatar_url:
#     #         profile.bio = bio
#     #         profile.avatar_url = avatar_url
#     #         profile.save()
#     #     return instance