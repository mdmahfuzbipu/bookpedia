import uuid
from django.db import models
from django.urls import reverse

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
    
    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
    