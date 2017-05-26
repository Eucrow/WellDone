from itertools import chain

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import UserSerializer, ProfileSerializer
from users.models import Profile


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
        profile_data = Profile.objects.get(pk=pk)
        user_data = get_object_or_404(User, pk=pk)

        serializer_profile = ProfileSerializer(profile_data)
        serializer_user = UserSerializer(user_data)

        return Response(serializer_profile.data)


    def delete(self, request, pk):
        """
        Function to delete user
        :param request:
        :param pk: id of the user to delete
        :return: JSON with successful or error message
        """

        user_authenticated = User(request.user.pk)

        #TODO: esto es una chapuza, lo de convertir el pk en entero
        if user_authenticated.pk == int(pk):

            try:
                user = User.objects.get(pk=pk)
            except User.DoesNotExist:
                user = None

            if user is not None:
                user.delete()
                message = {'Message': _('User deleted')}
                return Response(message)
            else:
                message = {'Error': _('User does not exists')}
                return Response(message)
        else:
            message = {'Error': _('You don´t have permission to remove this user')}
            return Response(message)
