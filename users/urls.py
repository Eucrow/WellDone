from users.views import SignUpView, SignUpSuccessView
from django.conf.urls import url


urlpatterns = [
    # web urls
    url(r'^signup$', SignUpView.as_view(), name='signup'),
    url(r'^signup_success$', SignUpSuccessView.as_view(), name='signup_success'),
]