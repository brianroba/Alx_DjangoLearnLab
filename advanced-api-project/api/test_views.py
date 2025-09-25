from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for auth-required tests
        self.user = User.objects.create_user(username='testuser', password='testpass123')

        # Create an author
        self.author = Author.objects.create(name="Test Author")

        # Create some books
        self.book1 = Book.objects.create(title="Book One", publication_year=2000, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2010, author=self.author)

        # URLs
        self.list_url = reverse('book-list')  # update with your URL name for list view
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Auth required

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_update_book(self):
        self.client.login(username='testuser', password='testpass123')
        data = {
            "title": "Updated Book",
            "publication_year": 2005,
            "author": self.author.id
        }
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.delete(self.detail_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books(self):
        response = self.client.get(self.list_url, {'publication_year': 2010})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book Two')

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_ordering_books(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # First book should be Book Two (2010)
        self.assertEqual(response.data[0]['title'], 'Book Two')
