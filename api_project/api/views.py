from django.shortcuts import render
from rest_framework import viewsets , generics
from .models import Book 
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class  BookViewSet(viewsets.ModelViewSet): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]



class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]



