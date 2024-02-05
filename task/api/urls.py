from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, PostAPIView, PostDetailAPIView, AllPostAPIView

router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostAPIView.as_view(), name='posts'),
    path('posts/<id>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('post/all/', AllPostAPIView.as_view()), 
]