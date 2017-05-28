from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from django.utils.translation import ugettext as _
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import ProfileSerializer, UserSerializer
from users.models import UserProfile


class UserAPI(APIView):
    def get(self, request, pk):
        """
        Get all the user data: from user model and profile model
        :param request: 
        :param pk: 
        :return: 
        """

        # Esto es lo que le he preguntado a Alberto, que no soy capaz de que me devuelva los
        # datos de los dos modelos a la vez:
        profile_data = UserProfile.objects.get(pk=pk)

        # serializer_profile = ProfileSerializer(profile_data)
        serializer_profile = UserSerializer(profile_data)

        return Response(serializer_profile.data)

    def delete(self, request, pk):
        """
        Function to delete user
        :param request:
        :param pk: id of the user to delete
        :return: JSON with successful or error message
        """
        user = get_object_or_404(User, pk=pk)

        self.check_object_permissions(request, user)

        user.delete()
        message = {'Message': _('User deleted')}
        return Response(message)
