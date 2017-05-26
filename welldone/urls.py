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

from welldone.views import ProfileDetailProxy, MyProfileDetailProxy, PostAPIView, CreatePostAPIView


from users import urls as users_urls

from welldone.views import ProfileDetailProxy, MyProfileDetailProxy, PostAPIView, CreatePostAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(users_urls)),
    url(r'^$', PostAPIView.as_view(), name='posts_list'),

    #conexion al microservicio de posts
    url(r'^new-post$', CreatePostAPIView.as_view(), name='create_post'),

    #conexión con microservicio de profiles
    url(r'^api/detail/(?P<pk>.+)$', ProfileDetailProxy.as_view()),
    url(r'^api/detail$', MyProfileDetailProxy.as_view()),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
