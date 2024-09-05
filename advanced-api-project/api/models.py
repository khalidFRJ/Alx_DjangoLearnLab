from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=100)  # Field to store the author's name

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book.
    """
    title = models.CharField(max_length=200)  # Field for the book's title
    publication_year = models.IntegerField()  # Field for the year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Foreign key linking to the Author model

    def __str__(self):
        return self.title
