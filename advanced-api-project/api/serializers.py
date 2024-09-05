from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Serializes all fields of the Book model.
    Includes custom validation for the publication_year.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation to ensure publication_year is not in the future.
        """
        from datetime import date
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes the name field and a nested BookSerializer to serialize related books.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serializer to dynamically include related books

    class Meta:
        model = Author
        fields = ['name', 'books']
