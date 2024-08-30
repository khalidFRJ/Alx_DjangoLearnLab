from django.urls import path 
from .import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet , BookList
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
      path('', include(router.urls)),
      path('book', BookList.as_view(), name='book-list'),
       path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
