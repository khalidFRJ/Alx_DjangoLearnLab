from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .seriealizers import BookSerializer

# Create your views here.


class BookListView(generics.ListAPIView):
    """
    View for retrieving all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    """
    View for retrieving a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    """
    View for adding a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    """
    View for modifying an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.DestroyAPIView):
    """
    View for removing a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer