from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .seriealizers import BookSerializer
from django_filters import rest_framework

class BookListView(generics.ListAPIView):
    """
    View for retrieving all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    """
    View for retrieving a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users

class BookCreateView(generics.CreateAPIView):
    """
    View for adding a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can add a new book

class BookUpdateView(generics.UpdateAPIView):
    """
    View for modifying an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update a book

class BookDeleteView(generics.DestroyAPIView):
    """
    View for removing a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete a book

from rest_framework.filters import SearchFilter

class BookListView(generics.ListAPIView):
    ...
    filter_backends = [ filters.SearchFilter]
    search_fields = ['title', 'author']

from rest_framework.filters import OrderingFilter

class BookListView(generics.ListAPIView):
    ...
    filter_backends =  ["filters.OrderingFilter"]
    ordering_fields = ['title', 'publication_year']

