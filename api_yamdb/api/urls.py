from django.urls import include, path
from rest_framework.routers import DefaultRouter

from content.views import CategoryViewSet, TitleViewSet, GenreViewSet
from review.views import ReviewViewSet, CommentViewSet

router_v1 = DefaultRouter()

router_v1.register('categories', CategoryViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]