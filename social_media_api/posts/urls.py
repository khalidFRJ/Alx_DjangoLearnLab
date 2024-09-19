from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls

from django.urls import path
from .views import UserFeedView

urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user_feed'),
]

