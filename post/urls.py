from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from post.views import HomeView, UserPostsView

from post.api import PostViewSet

router = DefaultRouter()
# router.register('api/1.0/blogs/(?P<blogger>[a-z0-9_-]+)', UserPostsViewSet, base_name='api_user_posts')

routerApi = SimpleRouter()
routerApi.register(r'^api/0.1/postlist', PostViewSet, 'Post')

urlpatterns = [
    #Web URLs
    url(r'^$', HomeView.as_view(), name='post_home'),
    url(r'^post/(?P<blogger>[a-z0-9_-]+)/$', UserPostsView.as_view(), name='post_usersposts'),

    #API URLs
    url('', include(router.urls)),
    url('', include(routerApi.urls))
]