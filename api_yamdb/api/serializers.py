from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from review.models import Category, Genre, Title, Review, Comment


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


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категория"""

    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для жанра"""
    class Meta:
        fields = '__all__'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор для произвидения"""
    category = SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )
    genre = SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )

    class Meta:
        model = Title
        fields = '__all__'


class ReadOnlyTitleSerilizer(serializers.ModelSerializer):
    """Сериализатор счёта рейтинга для произвидения"""
    rating = serializers.IntegerField(
        source='reviews__score__avg', read_only=True
    )
    category = CategorySerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Title
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    review_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment