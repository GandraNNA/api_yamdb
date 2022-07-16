from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

routerv1 = DefaultRouter()
routerv1.register('categories', CategoryViewSet, basename='titles')
routerv1.register('genres', GenreViewSet, basename='genres')
routerv1.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(routerv1.urls)),
]
