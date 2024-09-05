from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book/list'),                # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book/detail'),   # Retrieve a single book by ID
    path('books/new/', BookCreateView.as_view(), name='book/create'),        # Add a new book
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book/update'), # Modify an existing book
    path('books/<int:pk>/remove/', BookDeleteView.as_view(), name='book/delete'), # Remove a book
]
