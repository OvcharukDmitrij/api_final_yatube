from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, permissions, viewsets
from rest_framework.exceptions import NotFound, ParseError, PermissionDenied
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Follow, Group, Post, User

from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.')
        instance.delete()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        current_post = get_object_or_404(
            Post,
            id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=current_post)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.')
        instance.delete()

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = Post.objects.filter(id=post_id)
        if not post:
            raise NotFound()
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowList(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        author = User.objects.get(
            username=serializer.initial_data['following'])
        user = self.request.user
        if user == author:
            raise ParseError(
                'Нельзя подписаться на самого себя.')
        serializer.save(user=self.request.user)

    def get_queryset(self):
        new_queryset = Follow.objects.filter(user=self.request.user)
        return new_queryset
