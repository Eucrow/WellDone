from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from django.utils.translation import ugettext as _

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import UserSerializer


class UserAPI(APIView):
    def post(self, request):
        """
        Function to add user
        :param request: request with the users information
        :return: data saved + status ok or error 400
        """

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():  # si el usuario es válido
            new_user = serializer.save()  # grabamos el nuevo usuario
            return Response(serializer.data,
                            status.HTTP_201_CREATED)  # devolvemos lo que hemos grabado en la base de datos (es opcional)
            # y un mensaje 201 de que ha sido creado
        else:
            return Response(serializer.errors,
                            status.HTTP_400_BAD_REQUEST)  # si hay en error, el serializer lo guarda en serializers.error

    def delete(self, request, pk):
        """
        Function to delete user
        :param request:
        :param pk: id of the user to delete
        :return: JSON with successful or erroneous message
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
