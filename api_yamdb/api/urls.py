from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet, get_jwt_token, register)

router = DefaultRouter()
router.register(r"User", UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
