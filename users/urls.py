from users.api import UserAPI
from users.views import SignUpView, SignUpSuccessView, DeleteUserView
from django.conf.urls import url


urlpatterns = [
    # web urls
    url(r'^signup$', SignUpView.as_view(), name='signup'),
    url(r'^signup_success$', SignUpSuccessView.as_view(), name='signup_success'),
    url(r'^delete_user/(?P<pk>[0-9]+)$', DeleteUserView.as_view(), name="delete_user"),

    # api urls
    url(r'^api/0.1/signup$', UserAPI.as_view(), name="signup_api"),
    url(r'^api/0.1/delete_user/(?P<pk>[0-9]+)$', UserAPI.as_view(), name="delete_user_api")
]