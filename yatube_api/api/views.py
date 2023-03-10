from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet,\
    GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated,\
    IsAuthenticatedOrReadOnly
from rest_framework import filters

from posts import models
from . import serializers
from . permissions import IsOwnerPermissions


class BaseViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerPermissions)


class PostViewSet(BaseViewSet):
    queryset = models.Post.objects.select_related('author')
    serializer_class = serializers.Post

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.Group


class CommentViewSet(BaseViewSet):
    serializer_class = serializers.Comment

    def get_queryset(self, **kwargs):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(models.Post, pk=post_id)
        queryset = post.comments.select_related('author')
        return queryset

    def perform_create(self, serializer, *args):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(models.Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class Following(ListModelMixin, CreateModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.Follow
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.select_related('following')

    def perform_create(self, serializer, *args):
        serializer.save(user=self.request.user)
