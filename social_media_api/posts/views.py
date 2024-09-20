from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        followed_users = self.request.user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')


from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post  # Assuming you have a Post model

User = get_user_model()

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    user = request.user
    followed_users = user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    # Serialize the posts as needed
    return Response(posts)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like
from notifications.models import Notification

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        if Like.objects.filter(post=post, user=user).exists():
            return Response({'message': 'Already liked'}, status=400)
        Like.objects.create(post=post, user=user)
        # Create a notification
        Notification.objects.create(
            recipient=post.author, actor=user, verb='liked', target=post
        )
        return Response({'message': 'Post liked'})

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Like.objects.get_or_create(user=request.user, post=post)
        user = request.user
        like = Like.objects.filter(post=post, user=user).first()
        if not like:
            return Response({'message': 'Not liked yet'}, status=400)
        like.delete()
        return Response({'message': 'Post unliked'})
