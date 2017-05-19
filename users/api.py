from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import ProfilePermission


class UserAPI(APIView):

    def delete(self, request, pk):
        """
        Function to delete user
        :param request:
        :param pk: id of the user to delete
        :return: JSON with successful or erroneous message
        """
        user = get_object_or_404(User, pk=pk)

        self.check_object_permissions(request, user)

        user.delete()
        message = {'Message': _('User deleted')}
        return Response(message)

