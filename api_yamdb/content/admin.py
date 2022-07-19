from django.contrib import admin

from .models import Category, Genre, Title


admin.register(Category)
admin.register(Genre)
admin.register(Title)