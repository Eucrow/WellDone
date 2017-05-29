"""welldone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


from welldone import settings


from django.conf.urls.static import static

from welldone.views import PostAPIView, CreatePostAPIView, UserPostsAPIView, CreateCommentProxy

from users import urls as users_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostAPIView.as_view(), name='posts_home'),
    url(r'^blogs/(?P<blogger>[a-z0-9_-]+)/$', UserPostsAPIView.as_view(), name='post_usersposts'),
    url(r'', include(users_urls)),

    #conexion al microservicio de posts
    url(r'^new-post$', CreatePostAPIView.as_view(), name='create_post'),

    #conexion al microservicio de comments
    url(r'^create-comment$', CreateCommentProxy.as_view(), name='create_comment')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
