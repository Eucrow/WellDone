from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token

from users.api import UserAPI
from django.conf.urls import url, include

urlpatterns = [
    # We need an endpoint to delete user because rest-auth doesn't has it ???
    url(r'^api/delete_user/(?P<pk>[0-9]+)$', UserAPI.as_view(), name="delete_user_api"),

    #api JWT auth
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/api-token-refresh/', refresh_jwt_token),
    url(r'^api/api-token-verify/', verify_jwt_token),
]