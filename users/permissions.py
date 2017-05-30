# from rest_framework.permissions import BasePermission
#
#
# class ProfilePermission(BasePermission):
#     def has_permission(self, request, view):
#         """
#         Define si un usuario puede ajecutar cierto método o acceder cierta vista/controlador.
#         Los métodos y endpoints de rest_auth no necesitan tener asignados permisos.
#         Args:
#             request:
#             view: vista que se está ejecutando
#         Returns: True si el usuario puede acceder
#         """
#
#         from users.api import UserAPI
#         from welldone.views import \
#             MyProfileDetailProxy
#         ## tenemos que importarlo aquí para evitar un problema de importación cíclica
#
#         ## only authenticated users can make a DELETE request:
#         if request.method == "DELETE" and request.user.is_authenticated() and isinstance(view, UserAPI):
#             return True
#         ## only authenticated user can see the private profile
#         ## if request.method == "GET" and request.user.is_authenticated() and isinstance(view, MyProfileDetailProxy):
#         if request.method == "GET": #Lo modifico temporalmente para que me deje pasar
#             return True
#         if request.method == "POST": #Lo añado para que me deje crear posts
#             return True
#         ## only authenticated user can modify the profile
#         if request.method == "PUT" and request.user.is_authenticated() and isinstance(view, MyProfileDetailProxy):
#             return True
#
#         return False
#         ## el resto, no tiene permisos
#
#     def has_object_permission(self, request, view, obj):
#         """
#         Define si un usuario puede realizar la operación que quiere sobre el objeto obj
#         :param request:
#         :param view: vista que se está ejecutando
#         :param obj: objeto al que se quiere acceder
#         :return: True si el usuario puede realizar la acción
#         """
#         return request.user.is_superuser or request.user == obj


from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Indica si un usuario puede acceder a la vista que quiere
        :param request:
        :param view:
        :return:
        """
        from users.api import UserAPI
        if request.method == "POST":
            return True
        if request.user.is_superuser:
            return True
        if isinstance(view, UserAPI):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Indica si un usuario puede realizar una operacion sobre un objeto obj
        :param request:
        :param view:
        :param obj:
        :return:
        """
        return request.user.is_superuser or request.user == obj
