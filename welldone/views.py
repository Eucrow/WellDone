# -*- coding: utf-8 -*-
import json

from rest_framework_proxy.views import ProxyView


class MyProfileDetailProxy(ProxyView):
    """
    Proxy to authorizated user profile detail
    """
    proxy_host = 'http://127.0.0.1:9000'
    source = 'api/detail'

    # define dinámicamente las cabeceras que queremos enviar:
    def get_headers(self, request):
        headers = super(MyProfileDetailProxy, self).get_headers(request)
        if request.user.is_authenticated():
            user = {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "is_active": request.user.is_active,
                "is_staff": request.user.is_staff,
                "is_superuser": request.user.is_superuser
            }
            headers['Authorization'] = json.dumps(user)
        return headers


class ProfileDetailProxy(ProxyView):
    """
    Proxy to any public profile detail
    """
    proxy_host = 'http://127.0.0.1:9000'
    source = 'api/detail/%(pk)s'


class PostAPIView(ProxyView):
    proxy_host = 'http://127.0.0.1:9001'
    source = 'postList/'
    return_raw = True


class CreatePostAPIView(ProxyView):
    # Salto directamente al microservicio de post, para usar postman al crear no hace falta generar ninguna
    proxy_host = 'http://127.0.0.1:9002'

    source = 'api/1.0/posts/'
    return_raw = True