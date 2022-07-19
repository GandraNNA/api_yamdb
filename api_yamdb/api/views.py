from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import PageNumberPagination


from review.models import Category, Genre, Title, Review
from .mixins import CreateListDestroyViewSet
from .filters import TitlesFilter
from .permissions import (IsAdmin, IsAdminOrReadOnly,
                            IsAdminModeratorOwnerOrReadOnly)
from .serializers import (
    CategorySerializer, GenreSerializer, TitleSerializer,
    ReadOnlyTitleSerilizer, ReviewSerializer,
    CommentSerializer)


class CategoryViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(CreateListDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return ReadOnlyTitleSerilizer
        return TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    # TODO: добавить ещё проверок на Права доступа:
    #  Автор отзыва, модератор или администратор
    permission_classes = [IsAdminModeratorOwnerOrReadOnly]
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
    permission_classes = [IsAdminModeratorOwnerOrReadOnly]
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