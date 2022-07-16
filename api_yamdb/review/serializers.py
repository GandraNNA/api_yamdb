from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import Comment, Review, Title


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    review_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор отзывов с проверкой, что пользователь может
    оставить только один отзыв на произведение"""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    title = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Review

    def validate(self, data):
        if self.context['request'].method == 'PATCH':
            return data

        title = get_object_or_404(
            Title,
            pk=self.context['view'].kwargs['title_id']
        )
        review_qs = title.review.filter(
            author=self.context['request'].user)

        if review_qs.exists():
            raise ValidationError('Вы уже оставляли отзыв')

        return data
