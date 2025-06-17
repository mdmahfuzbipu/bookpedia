import uuid, html
from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Book
# Create your tests here.


class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            id=uuid.uuid4(),  
            title="Harry Potter and the Philosopher's Stone",
            author="J.K. Rowling",
            price=29.99,
            published_date=date(1997, 6, 26),
            description="A young wizard begins his journey.",
            rating=4.9,
            language="English",
            genre="Fantasy",
        )
    
    def test_book_str_method(self):
        self.assertEqual(str(self.book), "Harry Potter and the Philosopher's Stone by J.K. Rowling")

    def test_get_absolute_url(self):
        url = self.book.get_absolute_url()
        expected_url = reverse("book_detail", args=[str(self.book.id)])
        self.assertEqual(url, expected_url)

    def test_book_fields(self):
        self.assertEqual(self.book.title, "Harry Potter and the Philosopher's Stone")
        self.assertEqual(self.book.author, "J.K. Rowling")
        self.assertEqual(self.book.price, 29.99)
        self.assertEqual(self.book.published_date, date(1997, 6, 26))
        self.assertEqual(self.book.description, "A young wizard begins his journey.")
        self.assertEqual(self.book.rating, 4.9)
        self.assertEqual(self.book.language, "English")
        self.assertEqual(self.book.genre, "Fantasy")

    def test_book_list_view(self):
        """Test that book list view shows the book"""
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, html.escape(self.book.title))
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view(self):
        """Test the book detail view"""
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/00000000-0000-0000-0000-000000000000/")  # fake UUID
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, html.escape(self.book.title))
        self.assertTemplateUsed(response, "books/book_detail.html")
        self.assertEqual(no_response.status_code, 404)