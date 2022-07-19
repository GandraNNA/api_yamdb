from django.contrib.auth import get_user_model
from django.core.validators import (MinValueValidator,
                                    MaxValueValidator)
from django.db import models

from content.models import Title

User = get_user_model()


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='author'
    )
    # рейтинг отзыва от 1 до 10
    score = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(10),
                    MinValueValidator(1)))
    pub_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.text
