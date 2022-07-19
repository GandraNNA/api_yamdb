from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    title = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Review

    def validate(self, data):
        # пользователь может оставить только 1 отзыв на произведение
        author = self.context.get('request').user
        title_id = self.context.get('view').kwargs.get('title_id')
        if (self.context.get('request').method == 'POST'
                and Review.objects.filter(
                    title_id=title_id,
                    author_id=author.id
                ).exists()):
            raise ValidationError('Вы уже оставляли отзыв')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    review_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
