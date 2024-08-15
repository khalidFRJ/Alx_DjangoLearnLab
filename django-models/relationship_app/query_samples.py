# relationship_app/query_samples.py

from relationship_app.models import Book, Library, Librarian, Author

Library.objects.get(name=library_name)", "books.all()

Author.objects.get(name=author_name)", "objects.filter(author=author)

Librarian.objects.get(library=

def get_books_by_author(author_name):
    # Query all books by a specific author
    books = Book.objects.filter(author__name=author_name)
    return books

def list_books_in_library(library_name):
    # List all books in a library
    books = Book.objects.filter(library__name=library_name)
    return books

def get_librarian_for_library(library_name):
    # Retrieve the librarian for a library
    librarian = Librarian.objects.get(library__name=library_name)
    return librarian

if __name__ == "__main__":
    # Sample usage of the queries
    
    # Query books by a specific author
    author_name = "J.K. Rowling"
    books_by_author = get_books_by_author(author_name)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(book.title)
    
    # List books in a specific library
    library_name = "Central Library"
    books_in_library = list_books_in_library(library_name)
    print(f"Books in {library_name}:")
    for book in books_in_library:
        print(book.title)
    
    # Retrieve the librarian for a specific library
    librarian_name = get_librarian_for_library(library_name)
    print(f"Librarian for {library_name}: {librarian_name.name}")
