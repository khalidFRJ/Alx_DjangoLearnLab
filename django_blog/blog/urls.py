from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import (
    add_comment, CommentUpdateView, CommentDeleteView, PostDetailView ,
)
from .views import search
from .views import PostListByTagView 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comments/new/', add_comment, name='comment-add'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('tags/<slug:tag_slug>/', PostListByTagView.as_view(), name='posts_by_tag'),
    path('search/', search, name='search'),
]

