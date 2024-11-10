from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, PostViewSet

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]
