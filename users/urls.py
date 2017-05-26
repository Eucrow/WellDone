from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token
from users.api import UserAPI

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from users.views import BlogsView

router = DefaultRouter()

urlpatterns = [


    #Web URLs
    # url(r'^login$', LoginView.as_view(), name='users_login'),
    # url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    # url(r'^signup$', SignupView.as_view(), name='users_signup'),
    url(r'^blogs/$', BlogsView.as_view(), name='users_blogs'),

    #API URLs
    # url(r'^api/1.0/blogs$', BlogsListAPI.as_view(), name='api_blogslist'),
    # url(r'^api/1.0/users/(?P<blogger>[a-z0-9_-]+)$', UserDetailAPI.as_view(), name='api_userdetail'),
    # url(r'^api/1.0/signup$', SignupAPI.as_view(), name='api_signup'),

    # We need an endpoint to delete user because rest-auth doesn't has it
    url(r'^api/delete_user/(?P<pk>[0-9]+)$', UserAPI.as_view(), name="delete_user_api"),
    url(r'^api/user/(?P<pk>[0-9]+)$', UserAPI.as_view(), name="get_user_data"),

    # api JWT auth
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/api-token-refresh/', refresh_jwt_token),
    url(r'^api/api-token-verify/', verify_jwt_token),
    url(r'', include(router.urls))
]
