from users.views import SignUpView, SignUpSuccessView, DeleteUserView
from django.conf.urls import url


urlpatterns = [
    # web urls
    url(r'^signup$', SignUpView.as_view(), name='signup'),
    url(r'^signup_success$', SignUpSuccessView.as_view(), name='signup_success'),
    url(r'^delete_user/(?P<pk>[0-9]+)$', DeleteUserView.as_view(), name="delete_user"),
]