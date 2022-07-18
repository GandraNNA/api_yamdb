from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from content.models import Title
from .models import Review
from .serializers import ReviewSerializer, CommentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    # TODO: добавить ещё проверок на Права доступа:
    #  Автор отзыва, модератор или администратор
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    queryset = Review.objects.all()

    def get_queryset(self):
        # Возвращение запроса для отзыва
        title = get_object_or_404(
            Title,
            pk=self.kwargs.get('title_id')
        )
        return Review.objects.filter(title=title).all()

    def perform_create(self, serializer):
        # Сохранение отзыва
        title = get_object_or_404(
            Title,
            pk=self.kwargs.get('title_id')
        )
        serializer.save(
            author=self.request.user,
            title=title
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # TODO: добавить ещё проверок на Права доступа:
    #  Автор отзыва, модератор или администратор
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        # Получение комментариев или точного комментария,
        # если указан comment_id
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title=self.kwargs.get('title_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        # Сохранение автором комментария
        review_id = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title=self.kwargs.get('title_id')
        )
        serializer.save(
            author=self.request.user,
            review_id=review_id
        )
