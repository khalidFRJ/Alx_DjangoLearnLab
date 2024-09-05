from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .seriealizers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    View for retrieving all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users

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
