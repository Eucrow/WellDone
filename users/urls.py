from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token

from users.api import UserAPI
from users.views import SignUpView, SignUpSuccessView, DeleteUserView
from django.conf.urls import url, include

urlpatterns = [
    # web urls
    url(r'^signup$', SignUpView.as_view(), name='signup'),
    url(r'^signup_success$', SignUpSuccessView.as_view(), name='signup_success'),
    url(r'^delete_user/(?P<pk>[0-9]+)$', DeleteUserView.as_view(), name="delete_user"),

    # api urls
    url(r'^api/0.1/signup$', UserAPI.as_view(), name="signup_api"),
    url(r'^api/0.1/delete_user/(?P<pk>[0-9]+)$', UserAPI.as_view(), name="delete_user_api"),

    #api JWT auth
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/api-token-refresh/', refresh_jwt_token),
    url(r'^api/api-token-verify/', verify_jwt_token),
]