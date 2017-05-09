from django.contrib.auth.models import User

from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from rest_framework.response import Response


class UserAPI(APIView):

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
