from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create sample data
        self.book1 = Book.objects.create(title='Book One', author='Author A', publication_year=2021)
        self.book2 = Book.objects.create(title='Book Two', author='Author B', publication_year=2022)
        self.list_url = reverse('book-list')

    def test_create_book(self):
        # Test creating a new book
        data = {'title': 'Book Three', 'author': 'Author C', 'publication_year': 2023}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_read_book(self):
        # Test retrieving book list
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book(self):
        # Test updating a book
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        data = {'title': 'Updated Book One'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book One')

    def test_delete_book(self):
        # Test deleting a book
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        # Test filtering by title
        response = self.client.get(self.list_url, {'title': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        # Test searching by author
        response = self.client.get(self.list_url, {'search': 'Author A'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        # Test ordering by publication_year
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_permissions(self):
        # Test access without authentication (if required)
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Adjust depending on your authentication settings
