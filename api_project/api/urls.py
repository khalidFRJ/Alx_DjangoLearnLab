from django.urls import path 
from .import views


urlpatterns = [
    path('Book/', views.BookList.as_view(),name='BookList'),
]
