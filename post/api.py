from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from post.serializers import PostListSerializar
from post.views import PostQueryset


class PostViewSet(ModelViewSet):

    permission_classes = (IsAuthenticated,)
    search_fields = ('post_id', 'author', 'categories')
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        return PostQueryset.get_posts(self.request.user)

    def get_serializer_class(self):
        return PostListSerializar

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, post=self.request.post, categories=self.request.categories)

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user, post=self.request.post, categories=self.request.categories)


