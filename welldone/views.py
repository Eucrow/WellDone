# -*- coding: utf-8 -*-
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework_proxy.views import ProxyView
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound


class CommentProxy(ProxyView):
    """
    Proxy to create comment endpoint
    """
    proxy_host = 'http://127.0.0.1:9003'
    source = 'api/1.0/comment'
    return_raw = True



class PostAPIView(ProxyView):
    proxy_host = 'http://127.0.0.1:9001'
    source = 'postList/'
    return_raw = True


class CreatePostAPIView(ProxyView):
    permission_classes = (IsAuthenticated,)

    # Salto directamente al microservicio de post, para usar postman al crear no hace falta generar ninguna
    proxy_host = 'http://127.0.0.1:9002'
    source = 'api/1.0/posts/'
    return_raw = True

    def get_headers(self, request):
        headers = super(CreatePostAPIView, self).get_headers(request)
        if request.user.is_authenticated():
            # user = {
            #     "id": request.user.id,
            #     "username": request.user.username,
            #     "email": request.user.email,
            #     "first_name": request.user.first_name,
            #     "last_name": request.user.last_name,
            #     "is_active": request.user.is_active,
            #     "is_staff": request.user.is_staff,
            #     "is_superuser": request.user.is_superuser
            # }
            headers['Authorization'] = str(request.user.id)
        return headers


class UserPostsAPIView(ProxyView):
    proxy_host = 'http://127.0.0.1:9001'
    source = 'userPostList/'
    return_raw = True

    # def get_headers(self, request):
    #     headers = super(UserPostsAPIView, self).get_headers(request)
    #     if request.user.is_authenticated():
    #         headers['Authorization'] = str(request.user.id)
    #     return headers

    def get(self, request, *args, **kwargs):
        usuario = User
        usuario = User.objects.all().filter(username=self.kwargs["blogger"])
        if not usuario:
            return HttpResponseNotFound("No existe ningún blog con este nombre")
        else:
            self.get_headers(self, request, usuario.username, usuario.id )
        #     posts = self.get_queryset()
        #     context = {'posts_list': posts, 'blogger': self.kwargs["blogger"]}
        #     return render(request, 'post/user_posts.html', context)


    def get_headers(self, request, blogger, blogger_id):
        headers = super(UserPostsAPIView, self).get_headers(request)
        headers['X-Blogger'] = blogger
        headers['X-BloggerId'] = str(blogger_id)
        return headers