# -*- coding: utf-8 -*-
import json

from django.http.response import HttpResponse
from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework_proxy.views import ProxyView
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
import requests


class CommentProxy(ProxyView):
    """
    Proxy to create comment endpoint
    """
    proxy_host = 'http://127.0.0.1:9003'
    source = 'api/1.0/comment%(url)s'
    return_raw = True

    def get_headers(self, request):
        headers = super(CommentProxy, self).get_headers(request)
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


class PostAPIView(ProxyView):
    proxy_host = 'http://127.0.0.1:9001'
    source = 'postList/'
    return_raw = True


class CreatePostAPIView(ProxyView):
    permission_classes = (IsAuthenticated,)

    # Salto directamente al microservicio de post, para usar postman al crear no hace falta generar ninguna web
    proxy_host = 'http://127.0.0.1:9002'
    source = 'api/1.0/posts/'
    return_raw = True

    def get_headers(self, request):
        headers = super(CreatePostAPIView, self).get_headers(request)
        if request.user.is_authenticated():
            user = {
                "id": request.user.id,
                "username": request.user.username,
                # "email": request.user.email,
                # "first_name": request.user.first_name,
                # "last_name": request.user.last_name,
                # "is_active": request.user.is_active,
                # "is_staff": request.user.is_staff,
                # "is_superuser": request.user.is_superuser
            }
            headers['Authorization'] = json.dumps(user)
            # Como en la cabecera se le pasa el id del usuario y el username, esas dos líneas no hacen falta para crear el post:
            #headers['Authorization'] = str(request.user.pk)
            #headers['X-Username'] = request.user.username
        return headers


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        url = 'http://127.0.0.1:9001/postDetail/'
        headers = {
            'X-BLOGGER': self.kwargs["blogger"],
            'X-POSTID': self.kwargs["pk"]
        }
        response = requests.get(url, headers=headers)
        return HttpResponse(response.text, status=response.status_code)



class UserPostsAPIView(View):

    def get(self, request, *args, **kwargs):
        if not User.objects.filter(username=self.kwargs["blogger"]).exists():
            return HttpResponseNotFound("No existe ningún blog con este nombre")
        else:
            usuario = User.objects.get(username=self.kwargs["blogger"])
            url = 'http://127.0.0.1:9001/userPostList/'
            headers = {
                'XBLOGGER': usuario.username,
                'XBLOGGERID': str(usuario.id)
            }
            response = requests.get(url, headers=headers)
            return HttpResponse(response.text, status=response.status_code)

