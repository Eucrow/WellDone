from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from post.views import HomeView, UserPostsView

router = DefaultRouter()
# router.register('api/1.0/blogs/(?P<blogger>[a-z0-9_-]+)', UserPostsViewSet, base_name='api_user_posts')

urlpatterns = [
    #Web URLs
    url(r'^$', HomeView.as_view(), name='post_home'),
    url(r'^blogs/(?P<blogger>[a-z0-9_-]+)/$', UserPostsView.as_view(), name='post_usersposts'),

    #API URLs

    url('', include(router.urls))
]