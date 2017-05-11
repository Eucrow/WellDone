from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from comentary.serializers import ComentarySerializar
from comentary.views import ComentaryQueryset


class ComentaryViewSet(ModelViewSet):

    permission_classes = (IsAuthenticated,)
    search_fields = ('com_id', 'author', 'post')
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        return ComentaryQueryset.get_comentaries(self.request.user)

    def get_serializer_class(self):
        return ComentarySerializar

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, post=self.request.post)

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user, post=self.request.post)


