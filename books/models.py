import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField()
    description = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    language = models.CharField(max_length=30, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)
    
    class Meta:
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["author"]),
            models.Index(fields=["published_date"]),
        ]
        permissions = [
            ("special_status", "Can read all books"),
        ]
    
    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
    

class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    
    review = models.CharField(max_length=500)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.review[:50]  # Return first 50 characters of the review