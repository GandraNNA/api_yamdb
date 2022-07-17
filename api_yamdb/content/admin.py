from django.contrib import admin

from .models import Category, Genre, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
    )
    list_editable = ('name',)
    search_fields = ('slug',)
    list_filter = ('slug',)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
    )
    list_editable = ('name',)
    search_fields = ('slug',)
    list_filter = ('slug',)
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
        'year',
        'genre',
        'category',
        'rating',
    )
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'


admin.register(Category, CategoryAdmin)
admin.register(Genre, GenreAdmin)
admin.register(Title, TitleAdmin)