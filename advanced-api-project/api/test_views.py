from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create two users
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.other_user = User.objects.create_user(username="otheruser", password="password123")

        # Create some sample books
        self.book1 = Book.objects.create(title="Django Basics", author="John Doe", publication_year=2020)
        self.book2 = Book.objects.create(title="Python Advanced", author="Jane Smith", publication_year=2021)

        # URLs
        self.list_url = reverse("book-list")
        self.detail_url = lambda pk: reverse("book-detail", args=[pk])

    # -------------------------
    # CRUD TESTS
    # -------------------------

    def test_list_books(self):
        """Anyone should be able to list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)
        # Check returned fields
        self.assertIn("title", response.data[0])
        self.assertIn("author", response.data[0])
        self.assertIn("publication_year", response.data[0])

    def test_retrieve_book_detail(self):
        """Anyone should be able to view a single book"""
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)
        self.assertEqual(response.data["author"], self.book1.author)
        self.assertEqual(response.data["publication_year"], self.book1.publication_year)

    def test_create_book_authenticated(self):
        """Authenticated users can create a book"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "New Book", "author": "Author X", "publication_year": 2022}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        # Check saved data matches response
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["author"], data["author"])
        self.assertEqual(response.data["publication_year"], data["publication_year"])

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a book"""
        data = {"title": "No Auth Book", "author": "Author Y", "publication_year": 2023}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        """Authenticated users can update a book"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Updated Django Basics", "author": "John Doe", "publication_year": 2020}
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Basics")
        # Check response matches updated data
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["author"], data["author"])
        self.assertEqual(response.data["publication_year"], data["publication_year"])

    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book"""
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # -------------------------
    # FILTER, SEARCH, ORDERING
    # -------------------------

    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.list_url}?author=John Doe")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["author"] == "John Doe" for book in response.data))

    def test_search_books_by_title(self):
        response = self.client.get(f"{self.list_url}?search=Python")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Python" in book["title"] for book in response.data))

    def test_order_books_by_year_desc(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

    # -------------------------
    # PERMISSIONS
    # -------------------------

    def test_permission_required_for_update(self):
        """Unauthenticated users cannot update"""
        data = {"title": "Hack Update", "author": "John Doe", "publication_year": 2020}
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permission_required_for_delete(self):
        """Unauthenticated users cannot delete"""
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
