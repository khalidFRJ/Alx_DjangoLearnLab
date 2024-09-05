from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/<int:pk>/', BookListView.as_view(), name='book/list'),                # List all books
    path('books/detail', BookDetailView.as_view(), name='book/detail'),   # Retrieve a single book by ID
    path('books/create', BookCreateView.as_view(), name='book/create'),        # Add a new book
    path('books/update', BookUpdateView.as_view(), name='book/update'), # Modify an existing book
    path('books/delete', BookDeleteView.as_view(), name='book/delete'), # Remove a book
]
